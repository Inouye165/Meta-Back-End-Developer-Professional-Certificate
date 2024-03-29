from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def say_hello(request):
    return HttpResponse('Hello world!')

def homepage(request):
    return HttpResponse('Welcome to Little Lemon!')

def display_date(request):
    date_joined= datetime.today().year
    return HttpResponse(date_joined)

def menu(request):
    text = """<h1 style = "color: #f4ce14;">Welcome to Little Lemon!</h1>"""
    return HttpResponse(text)