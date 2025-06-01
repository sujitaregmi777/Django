from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def workshop_list(request):
    

    template_name = "workshop/workshop_list.html"
    context = {
        "title" :"Workshop List" ,
        "workshops" : Workshop.objects.all(),
        "members" : Member.objects.all(),
        
    }
    return render(request, template_name ,context)

def workshop_details(request,id):


    template_name = "workshop/workshop_details.html"
    workshop = get_object_or_404(Workshop,id=id)
    members = get_object_or_404(Member,workshop=workshop)
    context = {
        'workshop' :workshop,
        'members' : member,
    }

    return render(request, template_name ,context)

def member_list(request):
    return render(request, template_name )