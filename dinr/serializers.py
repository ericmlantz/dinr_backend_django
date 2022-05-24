from rest_framework import serializers
from .models import User, Restaurant

class UserSerializer(serializers.HyperlinkedModelSerializer):
  matches = serializers.HyperlinkedRelatedField(
    view_name='matche_list',
    many=True,
  )

  class Meta:
    model = User
    fields = ['id','firstName','lastName','email','username','password','street_loc', 'apt_loc','city_loc','state_loc','zip_loc', 'matches']