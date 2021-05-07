from django.urls import path
from acc import views


urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_customer/', views.create_customer, name='create_customer'),

    path('create_project/<str:pk>/', views.create_project, name='create_project'),
    path('update_project/<str:pk>/', views.update_project, name='update_project'),
    path('delete_project/<str:pk>/', views.delete_project, name='delete_project')
]
