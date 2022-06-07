from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('название категории', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)

    class Meta:
        verbose_name = 'категория товаров'
        verbose_name_plural = 'категории товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField('наименование товара', max_length=256, unique=True)
    date_delivery = models.DateField("дата поступления")
    price = models.DecimalField('цена за штуку', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)
    provider_name = models.CharField('имя поставщика', max_length=256, unique=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name
