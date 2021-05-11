from django.db.models.signals import post_save
from django.contrib.auth.models import Group, User
from .models import Customer
from django.contrib.auth.models import Group

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='client')
        instance.groups.add(group)

        Customer.objects.create(user=instance,
                                name=instance.username,
                                )
        print('User has been created')
post_save.connect(customer_profile, sender=User)