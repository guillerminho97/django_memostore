# Generated by Django 3.0 on 2020-02-26 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
        ('categories', '0011_auto_20200226_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]
