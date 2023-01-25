from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    noGuest= models.SmallIntegerField()
    bookingDate = models.DateTimeField()
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.SmallIntegerField()