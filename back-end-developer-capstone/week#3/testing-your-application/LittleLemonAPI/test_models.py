from django.test import TestCase
from LittleLemonAPI.models import MenuItem

class MenuItemTestCase(TestCase):
    def test1_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        
        self.assertEqual(itemstr, "IceCream : 80")
        

        
    