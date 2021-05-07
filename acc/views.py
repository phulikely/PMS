from django.db.models.aggregates import Count
from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    projects = Project.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    # total_projects = projects.count()
    total_projects = Project.objects.values("name").annotate(Count("name")).count()
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

def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    projects = customer.project_set.all()
    print(projects)
    # project_count = projects.count()
    project_count1 = projects.values("name").annotate(Count("name")).count()
    print(Project.objects.values("name"))

    context = {'customer':customer,
                'projects':projects,
                'project_count':project_count1
    }
    return render(request, 'accounts/customer.html', context)

def create_project(request):

    context = {}
    return render(request, 'accounts/project_form.html', context)