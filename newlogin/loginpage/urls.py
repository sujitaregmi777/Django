from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(next_page='dashboard'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
     path('accounts/profile/', views.home, name='home'),
     path('accounts/register/', views.register, name='register'),
     path('', views.dashboard, name='dashboard')

]