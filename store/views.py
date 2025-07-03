from django.shortcuts import render, get_object_or_404

from category.models import Category
from store.models import Product

'''
when url-> store route here then the category_slug value will be  None so it goes to line no 18 directly and run
when url-> products_by_category route here then the category_slug will contain something so line no 14 come to scene 
'''
def store(request, category_slug=None):
    categories = None
    products   = None

    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)   # get object of Category having slug = category slug
        products   = Product.objects.all().filter(category=categories, is_available=True) # get all the objet having category=categories(from just above line)
        product_count = products.count()

    else:
        products= Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context= {
        'products'      : products,
        'product_count' : product_count
    }
    return render (request, 'store/store.html', context)



def product_detail(request, category_slug, product_slug):
    try:
        # we can access the product with product_slug also but for the url as it already contain category_slug so we just append product_slug into the url
        product = Product.objects.get(category__slug=category_slug, slug= product_slug)  #category__slug is to directly get the slug field from model of category

    except Exception as e:
        raise e

    context ={
        'product':product,
    }
    return render (request, 'store/product_detail.html',context)