from django.shortcuts import render
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework import generics

# Create your views here.

class MenuItemViewSet(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
class singleMenuItemViewSet(generics.RetrieveUpdateDestroyAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer