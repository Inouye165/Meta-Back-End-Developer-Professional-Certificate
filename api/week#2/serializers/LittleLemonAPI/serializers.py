from rest_framework import serializers

class MenuItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=5, decimal_places=2) # added during lesson 2:45
    inventory = serializers.IntegerField() # added during lesson 2:45
 