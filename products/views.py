from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

from products.models import Product, ProductCategory


def get_all_products(category_id=None):
    return Product.on_site.select_related().all()


def products(request, category_id=None):
    if category_id:
        products_list = Product.on_site.filter(category_id=category_id)
    else:
        products_list = get_all_products()

    context = {
        'title': 'продукты',
        'categories': ProductCategory.on_site.all(),
        'products': products_list,
        'site': get_current_site(request=request),
    }
    return render(request, 'products/goods_list.html', context)
