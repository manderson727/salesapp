from django import forms
from django.contrib.auth.models import User
from salesapp.models import Product, Customer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProductForm(forms.ModelForm):
    itemid = forms.CharField(max_length=128, help_text="Enter the itemid.")
    itemname = forms.CharField(max_length=128, help_text="Enter the item name.")
    brand = forms.CharField(max_length=128, help_text="Enter the brand.")
    price = forms.IntegerField(help_text="Enter the price.")
    notes = forms.CharField(max_length=250, help_text="Enter description of item.")
    image = forms.ImageField(help_text="Select an image.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Product
        fields = ('itemid', 'itemname', 'brand', 'price', 'notes', )

class CustomerForm(forms.ModelForm):
    accountnum = forms.CharField(max_length=128, help_text='Enter customer number.')
    name = forms.CharField(max_length=128, help_text='Enter customer name.')

    class Meta:
        model = Customer
        fields = ('accountnum', 'name', )
