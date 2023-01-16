from django.contrib import admin
from django.urls import path, include

from authy import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.logged, name='login '),
    path('logout', views.loggout_user, name='logout'),
    path('home', views.home, name='home'),


]