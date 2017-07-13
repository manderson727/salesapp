from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from salesapp.models import Customer, Product, CartItem
from salesapp.forms import UserForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from salesapp.forms import ProductForm, CustomerForm, ProductAddToCartForm
import datetime as date
from django.db.models import Q
import random
from django.contrib.auth.decorators import login_required

CART_ID_SESSION_KEY = 'cart_id'

def index(request):
    #return HttpResponse("Sales App index!")

    context_dict = {'boldmessage' : "index view message"}
    return render(request, 'salesapp/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Sales App About Page!")

    context_dict = {'boldmessage' : "about view message"}

    return render(request, 'salesapp/about.html', context=context_dict)

@login_required
def customers(request):
    customer_list = Customer.objects.all()
    context_dict = {'customers': customer_list}

    return render(request, 'salesapp/customers.html', context_dict)

@login_required
def products(request):
    product_list = Product.objects.all()
    context_dict = {'products': product_list}

    return render(request, 'salesapp/products.html', context_dict)

@login_required
def add_product(request):
    form = ProductForm(request.POST, request.FILES)

    if form.is_valid():
        #print(request.FILES)
        newProduct = form.save(commit=False)
        newProduct.image = request.FILES['image']
        form.save(commit=True)
        return products(request)
    else:
        print(form.errors)

    return render(request, 'salesapp/add_product.html', {'form': form})

@login_required
def add_customer(request):
    form = CustomerForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return customers(request)
    else:
        print(form.errors)

    return render(request, 'salesapp/add_customer.html', {'form': form})

@login_required
def show_product(request, product_name_slug):

    context_dict = {}

    try:

        product = Product.objects.get(slug=product_name_slug)
        print(product)

        context_dict['product'] = product

    except Product.DoesNotExist:

        context_dict['product'] = None

    return render(request, 'salesapp/singleproduct.html', context_dict)

@login_required
def search_form(request):
    return render(request, 'salesapp/search_form.html')

@login_required
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        Products = Product.objects.filter(Q(itemname__icontains=q) | Q(brand__icontains=q))
        return render(request, 'salesapp/search_results.html', {'Products': Products, 'query': q})
    else:
        return HttpResponse('Please submit a search title')

#------------------------------------------------------------------------------

@login_required
def remove_from_cart(request, product_name_slug):
    user = request.user.id
    context_dict = {}
    id = int(request.POST.get('id',1))
    print("---------------------")
    print("REMOVE")
    print(request)
    print(request.POST.get('id',1))
    print(id)
    print("---------------------")

    cart_item = CartItem(id=id, cart_id=_cart_id(request))
    print(cart_item.cart_id)
    if cart_item:
        cart_item.delete()

    cartItems = CartItem.objects.filter(user_id=user)
    context_dict['cartitems'] = cartItems

    return render(request, 'salesapp/cart.html', context_dict)

@login_required
def update_cart(request, product_name_slug):
    user = request.user.id
    context_dict = {}
    id = int(request.POST.get('id', 1))
    quantity = request.POST.get('quantity', 1)

    cart_item = CartItem.objects.get(id=id, cart_id=_cart_id(request))

    if cart_item:
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            remove_from_cart(request,product_name_slug)

    cartItems = CartItem.objects.filter(user_id=user)
    context_dict['cartitems'] = cartItems

    return render(request, 'salesapp/cart.html', context_dict)

@login_required
def show_cart(request):
    user = request.user.id
    context_dict = {}
    cartItems = CartItem.objects.filter(user_id=user)

    context_dict['cartitems'] = cartItems

    return render(request, 'salesapp/cart.html', context_dict)

@login_required
def add_CartItem(request, product_name_slug):
    context_dict = {}
    product = Product.objects.get(slug=product_name_slug)
    user = request.user.id

    quantity = request.POST.get('quantity',1)

    context_dict['product'] = product

    cartItems = get_cart_items(request)
    product_in_cart = False

    for cartItem in cartItems:
        if cartItem.itemid_id == product.id:
            #print("Update")
            cart = CartItem.objects.get(id=cartItem.id)
            cart.quantity = cartItem.quantity + int(quantity)
            cart.save()
            product_in_cart = True

    if not product_in_cart:
        #print("Create")
        ci = CartItem.objects.create(cart_id=_cart_id(request), date_added=date.date.today(), quantity=int(quantity), itemid_id=product.id, user_id=user)
        ci.save()
        context_dict['cartitem'] = ci

    return render(request, 'salesapp/singleproduct.html', context_dict)

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

def cart_distinct_item_count(request):
    return get_cart_items(request).count()

def get_cart_items(request):
    return CartItem.objects.filter(cart_id=_cart_id(request))

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
