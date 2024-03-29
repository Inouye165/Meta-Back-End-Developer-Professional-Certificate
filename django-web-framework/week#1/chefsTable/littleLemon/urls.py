from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, ),
    path('menu/<int:menu_id>/', views.menu, name='menu_by_id'),
]

