from django.urls import re_path, path
from . import views

urlpatterns = [
    path('menu_item/10', views.display_menu_item),
    re_path(r"^menu_item/([0-9]{2}/)$", views.display_menu_item),
    
    ]