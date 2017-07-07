import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','final.settings')

import django
django.setup()
from salesapp.models import Customer, Product

def populate():

    customers = {"0000087": "ARANGO CIGAR COMPANY - NORTHBROOK",
                "0002288": "DAVIDUS CIGARS, LTD - FREDERICK",
                "0000793": "OLD VIRGINIA TOBACCO COMPANY - MANASSAS",
                "0000410": "L.J. PERETTI CO., INC. - BOSTON",
                "0008568": "Shawal Inc. - Scarsdale"
    }

    for accnum, accname in customers.items():
        c = add_cust(accnum, accname)

    products = [{"itemid": "CASCH",
                 "itemname": "Ashton Churchill",
                 "brand": "Ashton Classic"},
                {"itemid": "CASMA",
                 "itemname": "Ashton Magnum",
                 "brand": "Ashton Classic"},
                {"itemid": "CASDM",
                 "itemname": "Ashton Double Magnum",
                 "brand": "Ashton Classic"},
                {"itemid": "CLADCNBEL",
                 "itemname": "La Aroma de Cuba El Jefe",
                 "brand": "La Aroma de Cuba"},
                {"itemid": "CSCELGR",
                 "itemname": "San Cristobal Elegancia Grandioso",
                 "brand": "San Cristobal"},
                {"itemid": "CSCRLEV",
                 "itemname": "San Cristobal Revelation Leviathan",
                 "brand": "San Cristobal"}]

    for prod in products:
        #print(prod)
        p = add_prod(prod["itemid"], prod["itemname"], prod["brand"])

def add_cust(accountnum, name):
    c = Customer.objects.get_or_create(accountnum=accountnum, name=name)[0]
    c.save()
    return c

def add_prod(itemid, itemname, brand):
    p = Product.objects.get_or_create(itemid=itemid, itemname=itemname, brand=brand)[0]
    p.save()
    return p

if __name__ == '__main__':
    print("Starting salesapp population script...")
    populate()
