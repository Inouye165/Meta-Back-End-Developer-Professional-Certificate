from django.http import HttpResponse
from django.shortcuts import render
from .models import Menu 

def menu(request):
    menu_items = Menu.objects.all()
    items_dict = {'menu': menu_items}
    return render(request, 'menu.html', items_dict)