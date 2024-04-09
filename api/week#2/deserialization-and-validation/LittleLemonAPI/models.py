from django.db import models

# Create your models here.

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255)
    
    def __str__(self)-> str:
        return self.title
class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()
<<<<<<< HEAD
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=2)
=======
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
>>>>>>> bb2785625a841b06349d035127a44f063c741e54
