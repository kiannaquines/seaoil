# Generated by Django 5.0.6 on 2024-07-08 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_warehouseproductmodel_warehouse_product_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InventoryModel',
        ),
    ]
