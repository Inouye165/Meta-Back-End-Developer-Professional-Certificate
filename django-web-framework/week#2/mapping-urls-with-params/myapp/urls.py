from django import urls
from django.urls import path
from myapp import views
urlpatterns = [
    path('dishes/<str:dish>', views.menuitem),
]