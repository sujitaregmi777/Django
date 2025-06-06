from django.shortcuts import render
from .models import *

def home(request):
    details = Data.objects.first()  
    return render(request, 'profilee/home.html', {'details': details})

def portfolio(request):
    projects = Data.objects.all()
    return render(request, 'profilee/portfolio.html', {'projects': projects})

def skills(request):
    skills = ["Python", "Django", "JavaScript"] 
    return render(request, 'profilee/skills.html', {'skills': skills})

def contact(request):
    details = Data.objects.first()
    return render(request, 'profilee/contact.html', {'details': details})

def about(request):
    details = Data.objects.first()
    return render(request, 'profilee/about.html', {'details': details})

def resume(request):
    details = Data.objects.first()
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()

    return render(request, 'profilee/resume.html', {
        'data': data,
        'education': education,
        'experience': experience,
        'skills': skills,
    })
