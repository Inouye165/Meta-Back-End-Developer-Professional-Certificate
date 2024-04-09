from django.urls import path
from .views import menu_items
from . import views
from django.shortcuts import get_list_or_404

urlpatterns = [
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>/', views.single_item),
]