from django import forms
from django.contrib.auth.models import User
from salesapp.models import Product, Customer, CartItem

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

class ProductAddToCartForm(forms.ModelForm):
    quantity = forms.IntegerField()
    #slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = CartItem
        fields = ('quantity', )

    # def __int__(self, request=None, *args, **kwargs):
    #     self.request = request
    #     super(ProductAddToCartForm, self).__int__(*args, **kwargs)
    #
    # def clean(self):
    #     if self.request:
    #         if not self.request.session.test_cookie_worked():
    #             raise forms.ValidationError("Cookies must be enabled.")
    #     return self.cleaned_data

