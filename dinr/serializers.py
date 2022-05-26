from rest_framework import serializers
from .models import User, Restaurant

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id','firstName','lastName','email','username','password','street_loc', 'apt_loc','city_loc','state_loc','zip_loc', 'matches']

class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Restaurant
    fields = ['id','rest_name','rest_logo','rest_desc','food_type','rest_url','rest_phone','rest_street', 'rest_apt','rest_city','rest_state','rest_zip']
