# Generated by Django 5.0.6 on 2024-09-22 07:29

import datetime
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('categogry_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('category_name', models.CharField(max_length=255)),
                ('category_date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('product_date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='SupplierModel',
            fields=[
                ('supplier_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('supplier_companyname', models.CharField(max_length=255)),
                ('supplier_address', models.TextField()),
                ('supplier_mobilenumber', models.CharField(max_length=255)),
                ('supplier_date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_address', models.TextField(blank=True, max_length=255, null=True)),
                ('user_type', models.TextField(choices=[('Cashier', 'Cashier'), ('Attendant', 'Attendant'), ('Manager', 'Manager')], default='Cashier')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SaleModel',
            fields=[
                ('sale_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('sale_amount', models.FloatField()),
                ('sale_quantity', models.IntegerField()),
                ('sale_customername', models.CharField(max_length=255)),
                ('sale_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('sale_date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('encoded_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('sale_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productmodel')),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('request_status', models.BooleanField(default=False)),
                ('requested_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('request_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('request_order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.salemodel')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='WarehouseProductModel',
            fields=[
                ('warehouse_product_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('warehouse_product_name', models.CharField(max_length=255)),
                ('warehouse_product_stock', models.IntegerField()),
                ('warehouse_product_description', models.TextField(max_length=355)),
                ('warehouse_product_picture', models.ImageField(upload_to='products/')),
                ('warehouse_product_status', models.TextField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active')),
                ('warehouse_product_date_added', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('warehouse_product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.categorymodel')),
                ('warehouse_product_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.suppliermodel')),
            ],
            options={
                'verbose_name': 'Warehouse Product',
                'verbose_name_plural': 'Warehouse Products',
                'ordering': ['-warehouse_product_date_added'],
            },
        ),
        migrations.AddField(
            model_name='productmodel',
            name='product_warehouse_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.warehouseproductmodel'),
        ),
    ]
