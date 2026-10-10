from django.shortcuts import render

def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

def subjects(request):
    return render(request, 'accounts/subjects.html')

def contact(request):
    return render(request, 'accounts/contact.html')

def register(request):
    return render(request, 'accounts/register.html')


def login_view(request):
    return render(request, 'accounts/login.html')