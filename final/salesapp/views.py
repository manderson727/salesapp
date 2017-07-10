from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from salesapp.models import Customer, Product, CartItem
from salesapp.forms import UserForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from salesapp.forms import ProductForm, CustomerForm, ProductAddToCartForm
import datetime as date
from django.db.models import Q
import random

CART_ID_SESSION_KEY = 'cart_id'

def index(request):
    #return HttpResponse("Sales App index!")

    context_dict = {'boldmessage' : "index view message"}
    return render(request, 'salesapp/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Sales App About Page!")

    context_dict = {'boldmessage' : "about view message"}

    return render(request, 'salesapp/about.html', context=context_dict)

def customers(request):
    customer_list = Customer.objects.all()
    context_dict = {'customers': customer_list}

    return render(request, 'salesapp/customers.html', context_dict)

def products(request):
    product_list = Product.objects.all()
    context_dict = {'products': product_list}

    return render(request, 'salesapp/products.html', context_dict)

def add_product(request):
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        #print(request.FILES)
        newProduct = form.save(commit=False)
        newProduct.image = request.FILES['image']
        form.save(commit=True)
        return index(request)
    else:
        print(form.errors)

    return render(request, 'salesapp/add_product.html', {'form': form})

def add_customer(request):
    form = CustomerForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)
    else:
        print(form.errors)

    return render(request, 'salesapp/add_customer.html', {'form': form})

def show_product(request, product_name_slug):

    context_dict = {}

    try:

        product = Product.objects.get(slug=product_name_slug)
        print(product)

        context_dict['product'] = product

    except Product.DoesNotExist:

        context_dict['product'] = None

    return render(request, 'salesapp/singleproduct.html', context_dict)

def search_form(request):
    return render(request, 'salesapp/search_form.html')

def search(request):
    if 'q' in request.GET: # and request.GET['q']:
        q = request.GET['q']
        Products = Product.objects.filter(Q(itemname__icontains=q) | Q(brand__icontains=q))
        return render(request, 'salesapp/search_results.html', {'Products': Products, 'query': q})
    else:
        return HttpResponse('Please submit a search title')

#------------------------------------------------------------------------------

def add_CartItem(request, product_name_slug):
    product = Product.objects.get(slug=product_name_slug)
    print(product)

    ci = CartItem.objects.create(cart_id=_cart_id(request), date_added=date.date.today(), quantity=1, itemid_id=2)
    ci.save()

    return render(request, 'salesapp/cart.html', {'Products': product})

# get the current user's cart id, sets new one if blank
def _cart_id(request):
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]

    return cart_id


#def add_CartItem(request, product_name_slug):
    # form = ProductAddToCartForm(request.POST)
    # product = Product.objects.get(slug=product_name_slug)
    # print(product.itemid)
    # print(form)
    #
    # form = ProductAddToCartForm(initial={'cart_id': 123, 'itemid':product.itemid})
    #
    # if form.is_valid():
    #     print("-----------------")
    #     #ci = CartItem.objects.create(cart_id=1, date_added=date.date.today(), quantity=1, itemid=product.itemid)
    #     #ci.save()#you save your model changes, not your form
    #
    #     form.save(commit=True)
    #     return index(request)
    # else:
    #     print(form.errors)
    #
    # return render(request, 'salesapp/cart.html', {'form': form})


    # form = ProductAddToCartForm(request.POST)
    # print(form.is_bound)
    # product = Product.objects.get(slug=product_name_slug)
    #
    # context_dict = {}
    # context_dict['product'] = product
    #
    # if request.method == 'POST':
    #     print('In Post')
    #     form = ProductAddToCartForm(initial={'cart_id': 123, 'date_added':date.date.today(), 'quantity': 1, 'slug':product.slug, 'id':product.id, 'itemid':product.itemid, 'itemid_id':2})
    #
    #     if form.is_valid():
    #         ci = CartItem.objects.create(cart_id=1, date_added=date.date.today(), quantity=1, itemid=p)
    #         ci.save() #you save your model changes, not your form
    #         return HttpResponseRedirect(reverse('your:url'))#your return the success url or the same
    #     else:
    #         print(form.errors)
    #         #here error, if form isn't valid
    # else:
    #     print('In Get')
    #     form = ProductAddToCartForm(request.POST)
    #
    # return render(request, 'salesapp/singleproduct.html', context_dict)

    # print('In add_CartItem --------------------')
    # #form = ProductAddToCartForm(request.POST)
    #
    # context_dict = {}
    # product = Product.objects.get(slug=product_name_slug)
    #
    # context_dict['product'] = product
    #
    # print("----------------------")
    # #print(form)
    # print(product)
    # print(product.slug)
    # print(product.id)
    # print(product.itemid)
    # print("----------------------")
    #
    # if request.method == 'POST':
    #     print("In Post")
    #     form = ProductAddToCartForm(request.POST)
    #     #form = ProductAddToCartForm(initial={'cart_id': 123, 'date_added':date.date.today(), 'quantity': 1, 'slug':product.slug, 'id':product.id, 'itemid':product.itemid, itemid_id:2})
    #     #form.save(commit=True)
    #     print(form)
    #     if form.is_valid():
    #         print(product)
    #         print('In form.is_valid()--------------------------------')
    #
    #         ci = CartItem.objects.create(cart_id=1, date_added=date.date.today(), quantity=1, itemid=product, itemid_id=2)
    #
    #         form.save(commit=True)
    #         return index(request)
    #     else:
    #         #print(form.errors)
    #         #print(form.non_field_errors)
    #         return render(request, 'salesapp/errors.html', {'form': form})
    #
    # if request.method == 'GET':
    #     form = ProductAddToCartForm()
    #     print("In Get")
    #     print(product)
    #
    # return render(request, 'salesapp/singleproduct.html', context_dict) #{'form': form})

# @login_required
# def restricted(request):
#     return HttpResponse("Since you're logged in, you can see this text!")
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('index'))
#def register(request):
#
#     registered = False
#
#     if request.method == 'POST':
#
#         user_form = UserForm(data=request.POST)
#
#         if user_form.is_valid():
#             user = user_form.save()
#
#             user.set_password(user.password)
#             user.save()
#
#             registered = True
#
#         else:
#             print(user_form.errors)
#     else:
#         user_form = UserForm()
#
#     return render(request, 'salesapp/register.html', {'user_form': user_form, 'registered': registered})
#
# def user_login(request):
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(username=username, password=password)
#
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Your SalesApp account is disabled.")
#         else:
#             print("Invalid login details: {0}, {1}".format(username, password))
#             return HttpResponse("Invalid login details supplied.")
#     else:
#         return render(request, 'salesapp/login.html', {})
