from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100, blank = True)
    contact = models.CharField('Phone number',max_length=300,)
    time = models.DateTimeField()
    count = models.IntegerField()
    notes = models.CharField(max_length = 300)
    
    def __str__(self):
        return self.name