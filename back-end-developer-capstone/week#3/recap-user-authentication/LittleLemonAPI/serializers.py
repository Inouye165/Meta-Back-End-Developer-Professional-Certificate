from rest_framework.serializers import ModelSerializer
from LittleLemonAPI.models import MenuItem

class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'