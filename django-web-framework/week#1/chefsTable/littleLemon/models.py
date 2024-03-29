from django.db import models

# Create your models here.
from django.db import models

class Menu(models.Model):
    cuisine = models.CharField(max_length=100)
    menu_item = models.CharField(max_length=100)

    def __str__(self):
        return self.menu_item
