from django.db import models

#operactions for a database
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=2083)
