from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import SimpleRouter

routers=SimpleRouter()
routers.register('categories',CategoryViewSet,basename='category')
routers.register('products',ProductViewSet,basename='product')
routers.register('customers',CustomerViewSet,basename='customer')

urlpatterns = [
    
]+routers.urls