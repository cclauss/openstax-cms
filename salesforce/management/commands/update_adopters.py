from django.core.management.base import BaseCommand, CommandError
from salesforce.salesforce import Salesforce
from salesforce.models import Adopter


class Command(BaseCommand):
    help = "update adopters from salesforce.com"

    def handle(self, *args, **options): 
        with Salesforce() as sf:
            sf_adopters = sf.adopters()
            for sf_adopter in sf_adopters:
                adopter, created = Adopter.objects.get_or_create(
                                                       sales_id=sf_adopter['Id'],
                                                       name=sf_adopter['Name'],
                                                       description=sf_adopter['Description'],
                                                       website=sf_adopter['Website'],)
                adopter.save()
            responce = self.style.SUCCESS("Successfully updated adopters")
        self.stdout.write(responce)

