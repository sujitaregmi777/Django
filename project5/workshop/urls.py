from django.urls import path
from . import views

urlpatterns = [
    path('', views.workshop_list, name='workshop_list'),
    path('memb/', views.member_list, name='member_list'),
    path('details/<int:id>', views.workshop_details, name='workshop_details'),



]