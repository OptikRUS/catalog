from django.urls import path

from products.views import ProductList

app_name = 'products'

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
]

