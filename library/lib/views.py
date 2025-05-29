
from django.shortcuts import render,get_object_or_404
from .models import *

def authors(request):
    data=Author.objects.all()
    print(data)
    return render(request,'lib/author.html',{'data':data})

def home(request):
    return render(request,'lib/home.html')

def books(request):
    data=Books.objects.all()
    return render(request,'lib/book.html',{'book':data})


def library(request,id):    
    book=get_object_or_404(Books,id=id)
    return render(request,'lib/library.html',{'book':book})

# def Author(request,id):
#     author = get_object_or_404(Author,id=id)
#     return render(request, 'lib/author.html',{'author':author})

