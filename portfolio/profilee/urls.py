from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),

]