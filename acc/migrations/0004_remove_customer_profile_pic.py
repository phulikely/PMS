# Generated by Django 3.2 on 2021-05-10 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0003_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]