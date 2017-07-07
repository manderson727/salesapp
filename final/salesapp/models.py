from django.db import models


class Customer(models.Model):
    accountnum = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Product(models.Model):
    itemid = models.CharField(max_length=128, unique=True)
    itemname = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)

    def __str__(self):
        return self.itemname
