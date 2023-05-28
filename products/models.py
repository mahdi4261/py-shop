from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=31)
    category = models.CharField(max_length=31)
    description = models.CharField(max_length=511)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=1023)


class Offer(models.Model):
    code = models.CharField(max_length=31)
    description = models.CharField(max_length=511)
    discount = models.FloatField()

