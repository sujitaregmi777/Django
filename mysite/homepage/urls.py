from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('skills/', skills, name='skills'),
    path('project/', project, name='project'),
    path('contact/', contact, name='contact'),
    

]
