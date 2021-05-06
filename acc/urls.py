from django.urls import path
from acc import views


urlpatterns = [
    path('', views.home),
    path('members/', views.members),
    path('customer/<str:pk>/', views.customer),
]
