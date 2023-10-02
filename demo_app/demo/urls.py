from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name="login"),
    #Production
    path('Preform/home', views.PreformHome, name="Home"),
    path('Preform/hot_Press',views.hot_Press, name='hot_Press'),
    #Planning
    path('Planning/home', views.planningHome, name="Home")
   
]