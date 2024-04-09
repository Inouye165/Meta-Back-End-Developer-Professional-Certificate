from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MenuItem
from .serializers import MenuItemSerializer # added during lesson 2:21
from django.shortcuts import get_object_or_404 # added during lesson 3:35
@api_view(['GET'])
def menu_items(request):
    items = MenuItem.objects.all()
    serialized_item = MenuItemSerializer(items, many=True) # added during lesson 2:21
    # return Response(items.values()) # removed during lesson 2:21
    return Response(serialized_item.data) # added during lesson 2:21

@api_view(['GET']) # added during lesson 3:01
def single_item(request, id):
    # item = MenuItem.objects.get(pk=id) # removed during lesson 3:39
    item = get_object_or_404(MenuItem, pk=id) # added during lesson 3:39
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)