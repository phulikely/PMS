from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    projects = Project.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_projects = projects.count()
    completed = projects.filter(status='Completed').count()
    incompleted = total_projects - completed

    context = {'projects':projects, 
                'customers':customers,
                'total_customers':total_customers,
                'total_projects':total_projects,
                'completed':completed,
                'incompleted':incompleted
            }

    return render(request, 'accounts/dashboard.html', context)

def members(request):
    members = Member.objects.all()

    return render(request, 'accounts/member.html', {'members':members})

def customer(request):
    return render(request, 'accounts/customer.html')