from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from salesapp.models import Customer, Product
from salesapp.forms import UserForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

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

def show_product(request, product_name_slug):

    context_dict = {}

    try:

        product = Product.objects.get(slug=product_name_slug)
        print(product)

        context_dict['product'] = product

    except Product.DoesNotExist:

        context_dict['product'] = None

    return render(request, 'salesapp/singleproduct.html', context_dict)



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
