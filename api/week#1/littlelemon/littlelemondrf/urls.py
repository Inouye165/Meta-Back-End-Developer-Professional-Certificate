from django.urls import path
from . import views

urlpatterns = [
    path('ratings', views.RatingList.as_view(), name='rating-list'),
]
