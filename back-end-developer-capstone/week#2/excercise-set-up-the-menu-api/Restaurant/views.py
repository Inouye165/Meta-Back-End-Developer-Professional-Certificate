from django.shortcuts import render
# from rest_framework.generics import ListCreatView
from .models import Menu
from .serializers import MenuSerializer
from rest_framework import generics


# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer