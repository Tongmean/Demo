from django.shortcuts import render

# Create your views here.
import datetime

now = datetime.datetime.now().strftime("%d/%m/%Y"+ "%H:%M:%S")


def login(request):

    return render(request, 'Home/login.html')
#Production Department
def PreformHome(request):

    return render(request, 'Preform/home.html', {"now":now})

#Planning Department
def planningHome(request):

    return render(request, 'Planning/home.html')