from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)  # Assuming you want last name too
    company = models.CharField(max_length=200)
    worksite = models.CharField(max_length=200)
    job_title = models.CharField(max_length=200)
    comments = models.TextField()  # TextField for longer comments
