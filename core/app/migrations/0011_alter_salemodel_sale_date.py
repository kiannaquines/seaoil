# Generated by Django 5.0.6 on 2024-07-08 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_salemodel_sale_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salemodel',
            name='sale_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
