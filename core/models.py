from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.contrib.auth.hashers import make_password
from random import randint
# Create your models here.

class CustomUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
     
        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)
    


class User(AbstractUser):
    username=models.CharField(max_length=100,unique=True)
    email=None
    
    objects=CustomUserManager()
    
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]