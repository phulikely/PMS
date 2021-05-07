from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import *


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
    # project_count = projects.count()
    project_count = projects.values("name").annotate(Count("name")).count()

    my_filter = ProjectFilter(request.GET, queryset=projects)
    projects = my_filter.qs

    context = {'customer':customer,
                'projects':projects,
                'project_count':project_count,
                'my_filter':my_filter
    }
    return render(request, 'accounts/customer.html', context)

def create_customer(request):
    form = CustomerForm()
    if request.method == "POST":
        #print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/customer_form.html', context)


def create_project(request, pk):
    ProjectFormSet = inlineformset_factory(Customer, Project, fields=('member', 'name', 'status'), extra=3)
    customer = Customer.objects.get(id=pk)
    form_set = ProjectFormSet(queryset=Project.objects.none(), instance=customer)
    #form = ProjectForm(initial={'customer':customer})
    if request.method == "POST":
        #print(request.POST)
        #form = ProjectForm(request.POST)
        form_set = ProjectFormSet(request.POST, instance=customer)
        if form_set.is_valid():
            form_set.save()
            return redirect('/')

    context = {'form_set':form_set}
    return render(request, 'accounts/project_form.html', context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        #print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('/')    
    
    context = {'form':form}
    return render(request, 'accounts/project_form.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')

    context = {'item':project}
    return render(request, 'accounts/delete.html', context)   