from django.shortcuts import render
from django.http import HttpResponse
from salesapp.models import Customer, Product

def index(request):
    #return HttpResponse("Sales App index!")

    context_dict = {'boldmessage' : "index view message"}
    return render(request, 'salesapp/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Sales App About Page!")

    context_dict = {'boldmessage' : "about view message"}

    return render(request, 'salesapp/about.html', context=context_dict)

def accounts(request):
    customer_list = Customer.objects.all()
    context_dict = {'customers': customer_list}

    return render(request, 'salesapp/accounts.html', context_dict)

def products(request):
    product_list = Product.objects.all()
    context_dict = {'products': product_list}

    return render(request, 'salesapp/products.html', context_dict)

