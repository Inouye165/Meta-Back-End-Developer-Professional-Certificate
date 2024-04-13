from django.urls import path
from .views import SayHello
from django.contrib import admin

urlpatterns = [
    path('', SayHello, name='SayHello'),
]
