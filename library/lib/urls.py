from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('authors/', authors, name='authors'),
    path('library/<int:id>', library, name='library'),
    path('books/', books, name='books'),

]
