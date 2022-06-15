from django.shortcuts import render

from django.contrib.auth.models import User
from .serializers import RegisterSerializer,MyTokenObtainPairSerializer
from rest_framework import generics

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     # Replace the serializer with your custom
#     serializer_class = CustomTokenObtainPairSerializer