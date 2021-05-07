from django.forms import ModelForm
from .models import Customer, Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'