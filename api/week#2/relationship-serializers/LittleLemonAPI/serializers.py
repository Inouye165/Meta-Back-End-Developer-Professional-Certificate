from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal

# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)
#     price = serializers.DecimalField(max_digits=5, decimal_places=2)
#     inventory = serializers.IntegerField()
<<<<<<< HEAD
 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
 
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    # category = serializers.StringRelatedField()
    category = CategorySerializer()
=======

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
>>>>>>> bb2785625a841b06349d035127a44f063c741e54
    class Meta:
        model = MenuItem
        fields = ('id', 'title', 'price', 'stock', 'price_after_tax')
        
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)