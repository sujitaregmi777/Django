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
        'skills': ['python', 'django', 'html', 'css']
    }
    template_name = 'homepage/skills.html'
    return render(request, template_name, context)