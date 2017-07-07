from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Sales App index!")

    context_dict = {'boldmessage' : "index view message"}

    return render(request, 'salesapp/index.html', context=context_dict)

def about(request):
    #return HttpResponse("Sales App About Page!")

    context_dict = {'boldmessage' : "about view message"}

    return render(request, 'salesapp/about.html', context=context_dict)
