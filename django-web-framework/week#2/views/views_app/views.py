from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    content = "<html><body><h1>Welcome to Little Lemon<br>By Ron<br>3-28-2024</h1></body></html>"
    return HttpResponse(content)    
