from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django import forms

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

class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)

    itemid = models.ForeignKey('Product', unique=False, related_name="products")
    user = models.ForeignKey(User, unique=False)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def name(self):
        return self.product.name

    def get_absolute_url(self):
        return self.itemid.get_absolute_url()

    @property
    def total(self):
        return self.quantity * self.itemid.price

    @property
    def price(self):
        return self.itemid.price
