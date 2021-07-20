from django.shortcuts import render

# Create your views here.
def base(request):
    templates_name='base.html'
    return render(request, templates_name)

def home(request):
    templates_name='app1/home.html'
    return render(request, templates_name)

def contact(request):
    templates_name='app1/contact.html'
    return render(request, templates_name)

def gallery(request):
    templates_name='app1/gallery.html'
    return render(request, templates_name)

def login(request):
    templates_name='app1/login.html'
    return render(request, templates_name)

def registration(request):
    templates_name='app1/registration.html'
    return render(request, templates_name)