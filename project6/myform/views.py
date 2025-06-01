from django.shortcuts import render
from .forms import *
# Create your views here.
  
def feedback(request):
    form = FeedbackForm()
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
    
     print(form.cleaned_data)
     form.save()
    return render(request, 'myform/feedback.html.html')

    context = {

        "form":form
    }
    template_name = 'myform/feedback.html'
    return render(request,template_name, context)



def index(request):
    form = ContactForm()
    form = ContactForm(request.POST or None)
    if form.is_valid():
    
     print(form.cleaned_data)
    return render(request, 'myform/thank_you.html')

    context = {

        "form":form
    }
    template_name = 'myform/forms.html'
    return render(request,template_name, context)
