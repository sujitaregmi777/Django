from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url = "login")
def dashboard(request):
    return HttpResponse("you can view this profile")


def profile(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not allowed.")
    context = {}
    return render(request, 'customauth/profile.html', context)

def hamro(request):
    if   not request.user.is_authenticated:
        return HttpResponse("get out.")
    context = {
        'message' : "hello"
    }
    return render(request, 'customauth/hamro.html', context)
