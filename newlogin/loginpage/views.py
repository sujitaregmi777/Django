from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import register


# Create your views here.

@login_required(login_url = "login")
def dashboard(request):
    return HttpResponse("you can view this profile")


def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("you are not allowed.")
    context = {}
    return render(request, 'loginpage/home.html', context)

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():    
        messages.success(request, "Account registered successfully! Please log in.")
        form.save()
        return redirect('login')
    return render(request, 'loginpage/register.html', {'form': form})
