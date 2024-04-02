from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=200)
    seats = models.IntegerField()

    def __str__(self):
        return self.name


# Woot woot! I just did this assigntment
# 4/1/2024 12:00:00 PM