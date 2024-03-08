from django.db import models

class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.DateTimeField('Enter the exact time!')
    
