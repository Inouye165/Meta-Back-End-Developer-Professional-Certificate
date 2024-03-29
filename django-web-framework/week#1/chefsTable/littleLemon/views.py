from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

def hello(request):
    return HttpResponse("Hello world!<br>From Ron<br>3-28-2024")

def menu_by_id(request, menu_id):
    menu = Menu.objects.get(id=menu_id)
    # return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine.")
    return render(request, 'menu_card.html', {'menu': menu})