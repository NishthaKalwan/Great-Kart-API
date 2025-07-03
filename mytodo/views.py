""" This is project level directory so it doesn't contain views.py already we have to create manually it """



from django.shortcuts import render

from store.models import Product


def home(request):
    products=Product.objects.all().filter(is_available=True)

    context={
        'products' : products
    }

    return render(request,'home.html',context)
