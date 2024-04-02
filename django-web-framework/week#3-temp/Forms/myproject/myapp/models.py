from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)  # Assuming you only need the name field for now
    # You can add more fields here like booking_date, contact_info, etc.
