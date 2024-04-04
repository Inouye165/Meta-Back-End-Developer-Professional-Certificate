from django.urls import path
from . import views

urlpatterns = [
    path('index2/<str:name>/', views.index2, name='index'),
    path('index2/', views.index2, name='index2'),
    # Add your new paths here
]
