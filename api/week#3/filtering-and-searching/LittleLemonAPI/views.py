from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from .models import MenuItem
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status   

# Create your views here.
@api_view(['POST','GET'])
def menu_items(request):
    if(request.method == 'GET'):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        print(category_name,' ',items[0].category)
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        serialized_item = MenuItemSerializer(items, many=True)
        if search:
            items = items.filter(title__icontains=search)
            serialized_item = MenuItemSerializer(items, many=True)
        return Response(serialized_item.data)
    elif(request.method == 'POST'):
        serialized_item = MenuItemSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.validated_data,status.HTTP_201_CREATED)
    
@api_view()
def single_item(request, id):
    # item = get_object_or_404(MenuItem.objects,id=id)
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)