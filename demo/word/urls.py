from django.urls import path
from .views import *

urlpatterns = [
    path("student",student_api, name="students"),
    path("department",department_api, name="departments")
]
