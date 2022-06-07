# Generated by Django 4.0.4 on 2022-06-07 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_provider_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='название категории')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'категория товаров',
                'verbose_name_plural': 'категории товаров',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.productcategory', verbose_name='категория'),
            preserve_default=False,
        ),
    ]