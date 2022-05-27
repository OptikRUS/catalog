from django.db import models


class Product(models.Model):
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
