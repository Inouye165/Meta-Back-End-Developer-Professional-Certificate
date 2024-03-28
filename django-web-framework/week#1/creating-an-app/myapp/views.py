from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('Hello, World!<br>From Ron<br>3-28-2024')
