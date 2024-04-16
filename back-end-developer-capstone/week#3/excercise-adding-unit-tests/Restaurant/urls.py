from django.db import models
from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('items/', views.MenuItemView.as_view()),  # Adjusted to match 'items/'
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
]