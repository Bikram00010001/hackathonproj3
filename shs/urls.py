from django.contrib import admin
from django.urls import path
from .views import index, about, connect, state_crops,expected,weather

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('connectwithus/', connect, name='connect_with_us'),
    path('state_crops/<str:state_name>/', state_crops, name='state_crops'),
    path('expected/', expected, name='expected'),
    path('weather/',weather,name='weather'),
    
  
    # path('expectedpage/', expectedpage, name='expectedpage')
]
