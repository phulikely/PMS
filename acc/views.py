from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/dashboard.html')

def projects(request):
    return render(request, 'accounts/projects.html')

def customer(request):
    return render(request, 'accounts/customer.html')