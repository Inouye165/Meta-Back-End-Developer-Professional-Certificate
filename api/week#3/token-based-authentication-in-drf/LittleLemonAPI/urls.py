from django.urls import path
from .views import menu_items
from . import views
from django.shortcuts import get_list_or_404
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('menu-items/', views.menu_items),
    path('menu-items/<int:id>/', views.single_item),
    path('secret/', views.secret),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]