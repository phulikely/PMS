from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default='nobody.jpg', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Member(models.Model):
    CATEGORY = (
        ('C#', 'C#'),
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('Frontends', 'Frontends'),
        ('Backends', 'Backends'),
        ('FullStack', 'FullStack'),
    )
    name = models.CharField(max_length=200, null=True)
    work_exp_year = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold'),
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    
    def __str__(self):
        return self.name    