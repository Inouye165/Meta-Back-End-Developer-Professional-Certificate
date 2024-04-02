from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order, name='order'),
    path('order/success/', views.order_success, name='order_success'), 
]
