from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('devices/', views.devices, name='devices'),
    path('config/', views.config, name='config'),
    path('verify/', views.verify, name='verify'),
    path('log/', views.log, name='log'),
]
