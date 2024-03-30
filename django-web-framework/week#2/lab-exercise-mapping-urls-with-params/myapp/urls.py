from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),

    path('pictures', views.pictures, name='pictures'),
    path('main/', views.home),
    path('say_hello/', views.say_hello),
    path('display_date/', views.display_date),
    path('menu/', views.menu),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),

]
