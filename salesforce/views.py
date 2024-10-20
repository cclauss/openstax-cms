from rest_framework import viewsets, filters
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse, Http404
from django.utils import timezone
from django.core.exceptions import MultipleObjectsReturned

from .models import School, AdoptionOpportunityRecord, Partner, SalesforceForms, ResourceDownload, SavingsNumber, PartnerReview
from .serializers import SchoolSerializer, AdoptionOpportunityRecordSerializer, PartnerSerializer, SalesforceFormsSerializer, ResourceDownloadSerializer, SavingsNumberSerializer, PartnerReviewSerializer

from salesforce.salesforce import Salesforce
from books.models import Book
from oxauth.functions import get_logged_in_user_uuid
from global_settings.functions import invalidate_cloudfront_caches


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.filter(visible_on_website=True)
    serializer_class = PartnerSerializer


class SalesforceFormsViewSet(viewsets.ModelViewSet):
    queryset = SalesforceForms.objects.all()
    serializer_class = SalesforceFormsSerializer


class ResourceDownloadViewSet(viewsets.ModelViewSet):
    queryset = ResourceDownload.objects.all()
    serializer_class = ResourceDownloadSerializer

    def perform_create(self, serializer):
        serializer.save(last_access=timezone.now())


class PartnerReviewViewSet(viewsets.ViewSet):
    @action(methods=['get'], detail=True)
    def list(self, request):
        """
        Optionally restricts the returned reviews to a given user,
        by filtering against a `user_id` query parameter in the URL.
        """
        # for a review to show up in the API, the partner should be visible and the review approved
        queryset = PartnerReview.objects.filter(partner__visible_on_website=True).exclude(status='Rejected')
        user_uuid = self.request.query_params.get('user_uuid', None)
        if user_uuid is not None:
            queryset = queryset.filter(submitted_by_account_uuid=user_uuid)

        serializer = PartnerReviewSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def post(self, request):
        try:
            try:
                review_object = PartnerReview.objects.get(partner=request.data['partner'],
                                                          submitted_by_account_uuid=request.data['submitted_by_account_uuid'])
            except MultipleObjectsReturned: # just in case they somehow were able to create more than 1
                review_object = PartnerReview.objects.filter(partner=request.data['partner'],
                                                          submitted_by_account_uuid=request.data[
                                                              'submitted_by_account_uuid']).first()
            serializer = PartnerReviewSerializer(review_object)
            return Response(serializer.data)
        except PartnerReview.DoesNotExist:
            serializer = PartnerReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                invalidate_cloudfront_caches('salesforce/partners/')
                return JsonResponse(status=201, data=serializer.data)
        return JsonResponse(status=400, data="wrong parameters")

    @action(methods=['patch'], detail=True)
    def patch(self, request):
        review_object = PartnerReview.objects.get(id=request.data['id'])
        serializer = PartnerReviewSerializer(review_object, data=request.data,
                                         partial=True)  # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save()
            # set review status to Edited so it will reenter the review queue
            review_object.status = 'Edited'
            review_object.save()
            invalidate_cloudfront_caches('salesforce/partners/')
            return JsonResponse(status=201, data=serializer.data)
        return JsonResponse(status=400, data="wrong parameters")

    @action(method=['delete'], detail=True)
    def delete(self, request):
        user_uuid = get_logged_in_user_uuid(request)
        if user_uuid:
            review_object = PartnerReview.objects.get(id=request.query_params['id'])
            if user_uuid == str(review_object.submitted_by_account_uuid) or user_uuid == -1: # -1 is returned by get_logged_in_user_uuid when bypass_sso_cookie_check = True
                review_object.status = 'Deleted'
                review_object.save()
                invalidate_cloudfront_caches('salesforce/partners/')
            serializer = PartnerReviewSerializer(review_object)
            return Response(serializer.data)
        else:
            return Response(status=403, data="SSO cookie not set")

    serializer_class = PartnerReviewSerializer


class SavingsNumberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This endpoint will only ever return one item, the latest updated savings.
    """
    serializer_class = SavingsNumberSerializer

    def list(self, request, *args, **kwargs):
        instance = SavingsNumber.objects.latest('updated')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class AdoptionOpportunityRecordViewSet(viewsets.ViewSet):
    @action(methods=['get'], detail=True)
    def list(self, request):
        account_uuid = request.GET.get('account_uuid', False)
        # a user can have many adoption records - one for each book
        queryset = AdoptionOpportunityRecord.objects.filter(account_uuid=account_uuid)
        book_list = []
        for record in queryset:
            student_nums = [record.fall_student_number or 0, record.spring_student_number or 0, record.summer_student_number or 0]
            book_list.append({"name": record.book_name , "students": str(max(student_nums))})
        data = {"Books": book_list}

        return JsonResponse(data)


def get_adoption_status(request):
    account = request.GET.get('id', False)

    if account:
        with Salesforce() as sf:
            q = sf.query("SELECT Adoption_Status__c FROM Contact WHERE Accounts_ID__c = '{}'".format(account))

            return JsonResponse(q)
    else:
        raise Http404('Must supply account id for adoption.')
