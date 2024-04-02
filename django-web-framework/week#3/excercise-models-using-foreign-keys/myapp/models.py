from django.db import models

class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink_name = models.CharField(max_length=200)  # Changed from 'drink'
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, related_name='drinks')
