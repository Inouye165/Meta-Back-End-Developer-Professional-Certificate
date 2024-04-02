from django.db import models

# Create your models here.
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()

# I mixed up projects so you will see an extra migration file in the migrations folder that 
# shows the wrong model name and fields.