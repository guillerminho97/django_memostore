# Generated by Django 3.0 on 2020-01-20 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
        ('categories', '0002_category_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
