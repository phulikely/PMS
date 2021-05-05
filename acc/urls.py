from django.urls import path
from acc import views


urlpatterns = [
    path('', views.home),
    path('projects/', views.projects),
    path('customer/', views.customer),
]
