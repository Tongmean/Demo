from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name="login"),
    #Production
    path('Preform/home', views.PreformHome, name="Home"),

    #Planning
    path('Planning/home', views.planningHome, name="Home")
   
]