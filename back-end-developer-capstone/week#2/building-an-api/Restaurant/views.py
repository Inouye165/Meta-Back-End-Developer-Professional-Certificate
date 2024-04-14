from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import menu, booking
from .serializers import menuSerializer, bookingSerializer

# Create your views here.
class bookingview(APIView):
    
    def get(self, request):
        items = booking.objects.all()
        serializer = bookingSerializer(items, many=True)
        return Response(serializer.data) #returning the data in JSON format
    
class menuview(APIView):
    
    def post(self, request):
        serializer = menuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
