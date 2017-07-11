"""final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from salesapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/', views.about, name='about'),
    url(r'customers/', views.customers, name='customers'),
    url(r'products/', views.products, name='products'),
    url(r'^add_product/$', views.add_product, name='add_product'),
    url(r'^add_customer/$', views.add_customer, name='add_customer'),
    url(r'^items/(?P<product_name_slug>[\w\-]+)/$', views.show_product, name='show_product'),
    url(r'^items/(?P<product_name_slug>[\w\-]+)/add/$', views.add_CartItem, name='add_CartItem'),
    url(r'^search-form/$', views.search_form, name="search_form"),
    url(r'^search/$', views.search, name="search"),
    #url(r'^cart/$', views.show_cart, name='show_cart'),
    #url(r'^register/$', views.register, name='register'),
    #url(r'^login/$', views.user_login, name='login'),
    #url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^restricted/', views.restricted, name='restricted'),
]
