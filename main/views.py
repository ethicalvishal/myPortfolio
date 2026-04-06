from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    response=render(request, "main/home.html")
    return response

def about(request):
    return render(request, "main/about.html")

def skills(request):
    return render(request, "main/skills.html")

def projects(request):
    return render(request, "main/projects.html")

def contact(request):
    form=ContactForm()
    return render(request, "main/contact.html", {'form':form})