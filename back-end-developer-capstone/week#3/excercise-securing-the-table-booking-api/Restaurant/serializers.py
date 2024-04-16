from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Menu, Booking, MenuItem
from django.contrib.auth.models import User

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'
        
