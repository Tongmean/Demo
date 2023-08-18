from django.shortcuts import render

# Create your views here.

def login(request):

    return render(request, 'Home/login.html')

def Home(request):

    return render(request, 'Production/home.html')