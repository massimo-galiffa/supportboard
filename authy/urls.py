from django.urls import path

from authy import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
]
