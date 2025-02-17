# Generated by Django 3.0 on 2020-02-27 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
        ('carts', '0005_auto_20200226_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='carts.CartProducts', to='products.Product'),
        ),
        migrations.AlterField(
            model_name='cartproducts',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
    ]
