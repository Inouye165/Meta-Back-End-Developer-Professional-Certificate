from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.Menu),
    path('about/', views.About),
]