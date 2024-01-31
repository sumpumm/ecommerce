from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()



class UserRegistrationSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    password2=serializers.CharField()
    
    def validate_username(self,value):
        user=User.objects.filter(username=value).exists()
        if user:
            raise serializers.ValidationError("USername already exists")
        

    
    def validate(self,attrs):
        if attrs.get('password')!=attrs.get('password2'):
            raise serializers.ValidationError({
                'error':'password doesnt match'
            })
        if len(attrs.get('password'))<8:
            raise serializers.ValidationError({
                'error':'password length must be more than 8'
            })
        return super().validate(attrs)
        

        
