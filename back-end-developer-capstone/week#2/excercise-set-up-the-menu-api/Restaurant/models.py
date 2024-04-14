from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.AutoField(primary_key=True) # AutoField type, primary key
    name = models.CharField(max_length=255) # string type, max length 255
    no_of_guests = models.IntegerField() # integer type, 6 digits
    bookingdate = models.DateField() # date type
    
    def __str__(self):
        return self.name
    
    
class Menu(models.Model):
    id = models.AutoField(primary_key=True) # AutoField type, primary key
    title = models.CharField(max_length=255) # string type, max length 255
    price = models.DecimalField(max_digits=10, decimal_places=2) # decimal type, max digits 10, decimal places 2
    inventory = models.IntegerField() # integer type, 5 digits
    
    def __str__(self):
        return self.title  
    