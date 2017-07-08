from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Customer(models.Model):
    accountnum = models.CharField(max_length=128, unique=True)
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    itemid = models.CharField(max_length=128, unique=True)
    itemname = models.CharField(max_length=128)
    brand = models.CharField(max_length=128)
    image = models.ImageField(upload_to='static/images/')
    notes = models.CharField(max_length=250)
    price = models.IntegerField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.itemname)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.itemname
