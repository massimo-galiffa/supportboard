from django.urls import path, include

from supportboard import views

urlpatterns = [
    path('support', views.support_request, name='support'),
    path('list', views.support_request_list, name='list'),

]