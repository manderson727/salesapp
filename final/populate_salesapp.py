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

    products = [{"itemid": "CACHCL",
                 "itemname": "Ashton Churchill",
                 "brand": "Ashton Classic",
                 "image": "static/images/CACHCL.png",
                 "price": 19,
                 "notes": "Ashton is one of the world’s premier cigar brands. In addition to being America’s best-selling super-premium cigar, Ashton is enjoyed by cigar lovers in over 50 countries all across the globe."},
                {"itemid": "CAAMA",
                 "itemname": "Ashton Aged Maduro",
                 "brand": "Ashton Classic",
                 "image": "static/images/CAAMA.png",
                 "price": 21,
                 "notes": "Ashton Aged Maduro is the most widely acclaimed, highly sought-after Maduro cigar in the world today."},
                {"itemid": "CAASYM",
                 "itemname": "Ashton Symmetry",
                 "brand": "Ashton Classic",
                 "image": "static/images/CAASYM.png",
                 "price": 23,
                 "notes": "Ashton is a world-class, premium luxury cigar brand. Widely regarded for quality, consistency and excellence, Ashton is sought after by cigar lovers around the world."},
                {"itemid": "CAAHRT",
                 "itemname": "Ashton Heritage",
                 "brand": "Ashton Classic",
                 "image": "static/images/CAAHRT.png",
                 "price": 25,
                 "notes": "Ashton Heritage Puro Sol is a rare treat indeed. Handmade in the Dominican Republic in the Fuente factory, these cigars smoke like a dream come true."},
                {"itemid": "CALADCEE",
                 "itemname": "La Aroma de Cuba Edicion Especial",
                 "brand": "La Aroma de Cuba",
                 "image": "static/images/CALADCEE.png",
                 "price": 27,
                 "notes": "La Aroma de Cuba Edicion Especial is a 93-rated masterpiece blended by the esteemed cigar-maker, Jose ‘Pepin’ Garcia."},
                {"itemid": "CALADCN",
                 "itemname": "La Aroma de Cuba Noblesse",
                 "brand": "La Aroma de Cuba",
                 "image": "static/images/CALADCN.png",
                 "price": 29,
                 "notes": "La Aroma de Cuba Noblesse is an exclusive release handmade in Estelí, Nicaragua by legendary cigar-maker Jose 'Pepin' Garcia to commemorate the success of the bestselling La Aroma de Cuba brand."},
                {"itemid": "CASCE",
                 "itemname": "San Cristobal Elegancia",
                 "brand": "San Cristobal",
                 "image": "static/images/CASCE.png",
                 "price": 31,
                 "notes":"San Cristobal Elegancia is patiently blended by Jose ‘Pepin’ Garcia in Estelí, Nicaragua and offers a marvelous introduction to Nicaraguan tobaccos."},
                {"itemid": "CASCO",
                 "itemname": "San Cristobal Ovation",
                 "brand": "San Cristobal",
                 "image": "static/images/CASCO.png",
                 "price": 33,
                 "notes": "San Cristobal is a premium brand patiently blended by legendary cigar-maker, Jose ‘Pepin’ Garcia in Estelí, Nicaragua, that has earned scores of devoted cigar lovers and top ratings over the years."},]

    for prod in products:
        #print(prod)
        p = add_prod(prod["itemid"], prod["itemname"], prod["brand"], prod["image"], prod["notes"], prod["price"])

def add_cust(accountnum, name):
    c = Customer.objects.get_or_create(accountnum=accountnum, name=name)[0]
    c.save()
    return c

def add_prod(itemid, itemname, brand, image, notes, price):
    p = Product.objects.get_or_create(itemid=itemid, itemname=itemname, brand=brand, image=image, notes=notes, price=price)[0]
    p.save()
    return p

if __name__ == '__main__':
    print("Starting salesapp population script...")
    populate()
