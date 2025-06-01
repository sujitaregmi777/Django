from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import CustomLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import register


# Create your views here.

@login_required(login_url = "login")
def dashboard(request):
        return render(request, 'loginpage/dashboard.html')



def home(request):
    if  request.user.is_authenticated:
        context = {

        }
    return render(request, 'loginpage/dashboard.html', context)

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():    
        messages.success(request, "Account registered successfully! Please log in.")
        form.save()
        return redirect('login')
    return render(request, 'loginpage/register.html', {'form': form})

def custom_login(request):
    form = CustomLoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            form.add_error(None, "Invalid credentials")

    return render(request, 'loginpage/dashboard.html', {'form': form})
