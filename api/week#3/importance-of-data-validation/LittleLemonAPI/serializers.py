from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory') # REMOVE FOR METHOD 2, BUT KEEP FOR METHOD 3

    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category_id = serializers.IntegerField(write_only=True)
    category = CategorySerializer(read_only=True)
    
    # Methood 3: Using validate_<field_name> method
    # def validate_price(self, value):
    #     if (value < 2):
    #         raise serializers.ValidationError('Price must be at least $2')
    # def validate_stock(self, value):
    #     if (value < 0):
    #         raise serializers.ValidationError('Stock must be at least 0')
    
    # Method 4: Using validate method
    # title = serializers.CharField(
    # max_length=255,
    # validators=[UniqueValidator(queryset=MenuItem.objects.all())]
    # )
    def validate(self, attrs):
        if attrs['price'] < 2:
            raise serializers.ValidationError('Price should not be less than 2.0')
        if attrs['inventory'] < 0:
            raise serializers.ValidationError('Stock cannot be negative')
        return super().validate(attrs)
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'stock', 'price_after_tax', 'category', 'category_id']
        # METHOD USIND UNIQUE VALIDATOR IN KWAARGS
        # extra_kwargs = {
        #     'title': {
        #         'validators': [
        #             UniqueValidator(
        #                 queryset=MenuItem.objects.all()
        #             )
        #         ],
        #     },
        # }
        # Method 1: Using validators
        # extra_kwargs = {
        #     'price': {'min_value': 2},
        #     'stock': {'source': 'inventory', 'min_value': 0}
        # }
        validators = [
            UniqueTogetherValidator(
            queryset=MenuItem.objects.all(),
            fields=['title', 'price']
            ),
            ]
    
    def calculate_tax(self, product: MenuItem):
        return product.price * Decimal(1.1)