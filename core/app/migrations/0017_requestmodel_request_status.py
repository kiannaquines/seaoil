# Generated by Django 5.0.6 on 2024-09-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_requestmodel_request_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestmodel',
            name='request_status',
            field=models.BooleanField(default=False),
        ),
    ]
