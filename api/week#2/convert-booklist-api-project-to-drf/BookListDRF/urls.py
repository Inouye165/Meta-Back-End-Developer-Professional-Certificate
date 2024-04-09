from django.urls import path
from .views import BookView
from . import views
urlpatterns = [
    path('books/', BookView.as_view(), name='book-list'),
    path('books/<int:pk>', views.SingleBookView.as_view()),
]