from django.contrib import admin
from salesapp.models import Customer, Product

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('accountnum', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('itemid', 'itemname', 'brand')

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
