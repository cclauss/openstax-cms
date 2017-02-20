from django.contrib.auth.models import Group


def save_profile(user, *args, **kwargs):
    # for now - setting email address to prevent issues, should update it
    # eventually
    if user:
        user.email = '{}@openstax.org'.format(user.username)
        user.save()


def update_email(user, response, *args, **kwargs):
    contact_infos = response.get('contact_infos')

    # grabbing the highest id in the email list to determine newest email
    newest_email = max(contact_infos, key=lambda x:x['id'])

    user.email = newest_email['value']
    user.save()


def update_role(user, response, *args, **kwargs):
    self_reported_role = response.get('self_reported_role')

    if self_reported_role == 'student':
        group, created = Group.objects.get_or_create(name=self_reported_role.title())
        group.user_set.add(user)
