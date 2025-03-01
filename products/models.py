from django.db import models

#operactions for a database
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('living_room', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('balcony', 'Balcony'),
    ]
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=2083)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='living_room')

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField()
    discount = models.FloatField()