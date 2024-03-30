from django.urls import path
from . import views


urlpatterns = [
    path('getuser/', views.qryview, name='qryview'),
    path("showform/", views.showform, name="showform"), 
]