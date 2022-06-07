from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'главная',
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    context = {
        'title': 'продукты',
        'categories': ProductCategory.objects.all(),
        'products': products
    }
    return render(request, 'products/goods_list.html', context)
