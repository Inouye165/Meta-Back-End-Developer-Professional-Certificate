from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink_name = models.Char(max_length=200) # changed drink to drink_name
    price = models.IntegerField()
    