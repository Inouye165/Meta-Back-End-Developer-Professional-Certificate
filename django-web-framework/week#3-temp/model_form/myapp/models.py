from django.db import models

# Create your models here.
class Logger(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    # shift = models.ChoiceField(choices=shifts)
    time_log = models.TimeField(help_text='Enter the exact time')