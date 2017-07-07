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

    products = {"CASCH": "Ashton Churchill",
                "CASMA": "Ashton Magnum",
                "CASDM": "Ashton Double Magnum",
                "CLADCNBEL": "La Aroma de Cuba El Jefe",
                "CSCELGR": "San Cristobal Elegancia Grandioso",
                "CSCRLEV": "San Cristobal Revelation Leviathan"
    }

    for itemid, itemname in products.items():
        p = add_prod(itemid, itemname)

def add_cust(accountnum, name):
    c = Customer.objects.get_or_create(accountnum=accountnum, name=name)[0]
    c.save()
    return c

def add_prod(itemid, itemname):
    p = Product.objects.get_or_create(itemid=itemid, itemname=itemname)[0]
    p.save()
    return p

if __name__ == '__main__':
    print("Starting salesapp population script...")
    populate()
