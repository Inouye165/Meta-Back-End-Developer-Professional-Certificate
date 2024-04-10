from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status   
from django.core.paginator import Paginator, EmptyPage
from rest_framework.decorators import permission_classes, throttle_classes,api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttles import TenCallsPerMinute


# Create your views here.
@api_view(['POST','GET'])
def menu_items(request):
    if(request.method == 'GET'):
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        print(category_name,' ',items[0].category)
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)
        if category_name:
            items = items.filter(category__title=category_name)
        if to_price:
            items = items.filter(price=to_price)
        if search:
            items = items.filter(title__icontains=search)
        if ordering:
            ordering_fields = ordering.split(',') 
            items = items.order_by(*ordering_fields) 
        paginator = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number = page)
        except EmptyPage:
            items = []
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

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message': 'secret message'})

@api_view()
@throttle_classes([AnonRateThrottle])   
def throttle_check(request):
    return Response({'message': 'successfull'})
    
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message": "message for authenticated users"})