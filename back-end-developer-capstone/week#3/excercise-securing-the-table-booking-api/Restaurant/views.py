from django.shortcuts import render
# from rest_framework.generics import ListCreatView
from .models import Menu, Booking, MenuItem
from .serializers import MenuSerializer, UserSerializer, BookingSerializer, MenuItemSerializer
from rest_framework import generics, permissions,viewsets
from django.contrib.auth.models import User
import rest_framework
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(rest_framework.viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer