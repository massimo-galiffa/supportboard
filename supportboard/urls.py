from django.urls import path

from supportboard import views

urlpatterns = [
    path('support', views.support_request, name='support'),
    path('list', views.support_request_list, name='list'),
    path('delete/<int:pk>', views.support_request_delete, name='delete'),
    path('support_requests/<int:pk>/', views.support_request_detail, name='detail'),
    path('update/<int:pk>', views.update_support_request, name='update'),
]
