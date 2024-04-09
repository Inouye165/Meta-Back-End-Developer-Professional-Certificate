from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal
# class MenuItemSerializer(serializers.Serializer): # This is the old way of doing it
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)
#     price = serializers.DecimalField(max_digits=5, decimal_places=2)
#     inventory = serializers.IntegerField()

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory') # added at 1:22 in video
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax') # added at 2:04 in video
    class Meta:
        model = MenuItem
        #fields = ['id', 'title', 'price','inventory'] # removed at 1:22 in video
        # fields = ['id', 'title', 'price','stock', 'price_after_tax']# removed at 2:04 in video
        fields = ['id', 'title', 'price','stock','price_after_tax'] # added at 2:04 in video

    def calculate_tax(self, product: MenuItem): # added at 2:04 in video
        return product.price * Decimal(1.1)