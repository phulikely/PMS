# Generated by Django 3.2 on 2021-05-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc', '0004_remove_customer_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]