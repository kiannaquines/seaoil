# Generated by Django 5.0.6 on 2024-07-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_invoicemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='warehouseproductmodel',
            name='warehouse_product_status',
            field=models.TextField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default=('Active', 'Active')),
        ),
    ]
