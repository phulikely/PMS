from django.db.models.aggregates import Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import ProjectForm, CustomerForm, CreateUserForm
from .filters import *
from .decorators import unauthenticated_user, allowed_users, admin_only


@unauthenticated_user
def login_page(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'accounts/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def register_page(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            # group = Group.objects.get(name='client')
            # user.groups.add(group)

            # Customer.objects.create(user=user)

            messages.success(request, 'Account created for ' + username + ' successfully')
            return redirect('login')
        else:
            messages.error(request, 'Account created unsuccessfully')

    context = {'form':form}
    return render(request, 'accounts/register.html', context)


@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
@admin_only
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def user_page(request):
    projects = request.user.customer.project_set.all()

    total_projects = projects.values("name").annotate(Count("name")).count()
    completed = projects.filter(status='Completed').count()
    incompleted = total_projects - completed

    context = {'projects':projects,
                'total_projects':total_projects,
                'completed':completed,
                'incompleted':incompleted,
                }
    return render(request, 'accounts/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def acc_settings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/acc_settings.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def members(request):
    members = Member.objects.all()

    return render(request, 'accounts/member.html', {'members':members})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('/')

    context = {'item':project}
    return render(request, 'accounts/delete.html', context)


def page_not_found(request):
    return render(request, 'accounts/page_not_found.html')