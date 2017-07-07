from django.contrib import admin
from salesapp.models import Customer, Product

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('accountnum', 'name')
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('itemid', 'itemname', 'brand', 'image')
    prepopulated_fields = {'slug':('itemname',)}

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
