from django.shortcuts import render

from products.models import Product, ProductCategory


def get_all_products(category_id=None):
    return Product.objects.select_related().all()


def products(request, category_id=None):
    if category_id:
        products_list = Product.objects.filter(category_id=category_id)
    else:
        products_list = get_all_products()

    context = {
        'title': 'продукты',
        'categories': ProductCategory.objects.all(),
        'products': products_list
    }
    return render(request, 'products/goods_list.html', context)
