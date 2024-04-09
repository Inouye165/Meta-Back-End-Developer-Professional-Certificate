from rest_framework import serializers
from .models import MenuItem
from decimal import Decimal
from .models import Category
# class MenuItemSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=100)
#     price = serializers.DecimalField(max_digits=5, decimal_places=2)
#     inventory = serializers.IntegerField()
<<<<<<< HEAD
 
=======
>>>>>>> bb2785625a841b06349d035127a44f063c741e54
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']
 
class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
<<<<<<< HEAD
    # category = serializers.StringRelatedField()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)  
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock','price_after_tax','category','category_id']
=======
    category = CategorySerializer()
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock','price_after_tax','category']
>>>>>>> bb2785625a841b06349d035127a44f063c741e54
        
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)