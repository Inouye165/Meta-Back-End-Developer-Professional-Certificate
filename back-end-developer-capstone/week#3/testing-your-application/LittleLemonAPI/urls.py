from django.urls import path
from .views import MenuItemViewSet, singleMenuItemViewSet
from rest_framework import routers
from . import views

urlpatterns = [
    path('menu-items/', MenuItemViewSet.as_view()),
    path('menu-items/<int:pk>/', singleMenuItemViewSet.as_view())   
]