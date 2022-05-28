from django.shortcuts import render
from django.views.generic.list import ListView

from products.models import Product


class ProductList(ListView):
    model = Product
    template_name = 'products/goods_list.html'
    title = 'Продукты'
