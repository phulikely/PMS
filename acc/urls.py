from django.urls import path
from acc import views


urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    path('page_not_found/', views.page_not_found, name='page_not_found'),

    path('account/', views.acc_settings, name='account'),

    path('', views.home, name='home'),
    path('user/', views.user_page, name='user_page'),

    path('members/', views.members, name='members'),
    path('customer/<str:pk>/', views.customer, name='customer'),
    path('create_customer/', views.create_customer, name='create_customer'),

    path('create_project/<str:pk>/', views.create_project, name='create_project'),
    path('update_project/<str:pk>/', views.update_project, name='update_project'),
    path('delete_project/<str:pk>/', views.delete_project, name='delete_project')
]
