# Generated by Django 5.0.6 on 2024-07-08 06:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_inventorymodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouseproductmodel',
            options={'ordering': ['-warehouse_product_date_added'], 'verbose_name': 'Warehouse Product', 'verbose_name_plural': 'Warehouse Products'},
        ),
        migrations.AlterField(
            model_name='warehouseproductmodel',
            name='warehouse_product_date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]