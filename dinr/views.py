from django.shortcuts import render
from .serializers import UserSerializer, RestaurantSerializer
from .models import User, Restaurant
from rest_framework import viewsets

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RestaurantView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer