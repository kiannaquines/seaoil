# Generated by Django 5.0.6 on 2024-07-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouseproductmodel',
            name='warehouse_product_status',
            field=models.TextField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active'),
        ),
    ]