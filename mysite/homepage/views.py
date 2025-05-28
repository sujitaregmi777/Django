from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context= {
        "page-title": "django day 3",
        "messages": "welcome"
    }
    return render(request, 'homepage/home.html', context)

def about(request):
    context= {

    }
    return render(request, 'homepage/about.html', context)

def skills(request):
    context = {

    }
    template_name = 'homepage/skills.html'
    return render(request, template_name, context)

def project(request):
    context= {

    }
    return render(request, 'homepage/project.html', context)

def contact(request):
    context= {

    }
    return render(request, 'homepage/contact.html', context)