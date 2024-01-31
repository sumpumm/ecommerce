from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User=get_user_model()



@api_view(['POST'])
def user_register(request):
    serializer=UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username=serializer.validated_data.get('username')
    password=serializer.validated_data.get('password')
    
    user=User.objects.create_user(username=username,password=password)
    if user:
    
        return Response('user has been created')
    
    return Response('something went wrong')    


@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    
    user=authenticate(username=username,password=password)
    
    if user:
        token,_=Token.objects.get_or_create(user=user)
        return Response({
            'user' :user.get_username(),
            'token':token.key
        })
    return Response("invalid")
            