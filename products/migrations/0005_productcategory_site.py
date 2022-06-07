# Generated by Django 4.0.4 on 2022-06-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('products', '0004_productcategory_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]