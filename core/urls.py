from django.contrib import admin
from django.urls import path,include
from .views import *



urlpatterns = [
  #path('register',user_register),
  #path('login',login),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.authtoken')),
    
    
]
    