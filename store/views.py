from django.shortcuts import render,get_object_or_404
from.models import Product
from category.models import Category
# Create your views here.
def store(request,category_slug=None):
    categories = None
    Products = None

    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories,is_available=True)
        product_count = products.count()

    else:

        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products':products,
        'count':product_count
    }
    return render(request, 'store/store.html',context)


def product_detail(request,category_slug,product_slug):
    return render(request, 'store/product_detail.html')