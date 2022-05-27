from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', ('price', 'quantity', 'provider_name'), 'date_delivery')
    search_fields = ('name', )
    ordering = ('price', )
