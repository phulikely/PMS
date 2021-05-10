from django.forms import ModelForm
from .models import Customer, Project
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from acc import models

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']