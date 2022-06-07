from django.contrib import admin
from products.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('category', 'name', ('price', 'quantity', 'provider_name'), 'date_delivery')
    search_fields = ('name', )
    ordering = ('price', )


@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)