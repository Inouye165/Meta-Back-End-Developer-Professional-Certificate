from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from .models import MenuItem
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status   
from django.core.paginator import Paginator, EmptyPage
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group

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
    
@api_view(['GET','POST'])
def single_item(request, id):
    # item = get_object_or_404(MenuItem.objects,id=id)
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({'message': 'secret message'})

# From API throttling for class-based views - First set of code
# class MenuItemsViewSet(viewsets.ModelViewSet):
#     throttle_classes = [AnonRateThrottle, UserRateThrottle]
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer
from .throttles import TenCallsPerMinute 
# From API throttling for class-based views - Second set of code
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [TenCallsPerMinute]
        else:
            throttle_classes = [AnonRateThrottle, UserRateThrottle]
        return [throttle() for throttle in throttle_classes]
    
@api_view(['POST','DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data.get('username')
    print(request.data)
    print('username = ', username)
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name='manager')
        print('after if: ',user)
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
    return Response({'message': 'ok'})
