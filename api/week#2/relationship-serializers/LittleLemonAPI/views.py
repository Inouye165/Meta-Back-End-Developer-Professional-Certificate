from .serializers import MenuItemSerializer
from rest_framework.decorators import api_view
from .models import MenuItem
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
 
# Create your views here.
@api_view(['POST','GET'])
def menu_items(request):
<<<<<<< HEAD
    # items = MenuItem.objects.all()
    items = MenuItem.objects.select_related('category').all() # Changed at 2:11
=======
    items = MenuItem.objects.all()
>>>>>>> bb2785625a841b06349d035127a44f063c741e54
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)

@api_view()
def single_item(request, id):
    item = get_object_or_404(MenuItem.objects,id=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)