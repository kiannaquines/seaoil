from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class CategoryModel(models.Model):
    categogry_id = models.AutoField(primary_key=True,unique=True)
    category_name = models.CharField(max_length=255)
    category_date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.category_name

class CustomUser(AbstractUser):

    USER_TYPE = (
        ('Cashier','Cashier'),
        ('Attendant','Attendant'),
        ('Manager','Manager'),
    )

    user_address = models.TextField(max_length=255,blank=True,null=True)
    user_type = models.TextField(choices=USER_TYPE,default=USER_TYPE[0][0])
    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
     
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class WarehouseProductModel(models.Model):
    WAREHOUSE_PRODUCT_STATUS = (
        ('Active','Active'),
        ('Inactive','Inactive')
    )
    warehouse_product_id = models.AutoField(primary_key=True,unique=True)
    warehouse_product_name = models.CharField(max_length=255)
    warehouse_product_stock = models.IntegerField()
    warehouse_product_description = models.TextField(max_length=355)
    warehouse_product_picture = models.ImageField(upload_to="products/")
    warehouse_product_supplier = models.ForeignKey('SupplierModel',on_delete=models.CASCADE)
    warehouse_product_category = models.ForeignKey('CategoryModel',on_delete=models.DO_NOTHING,null=True,blank=True)
    warehouse_product_status = models.TextField(choices=WAREHOUSE_PRODUCT_STATUS,default=WAREHOUSE_PRODUCT_STATUS[0][0])
    warehouse_product_date_added = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.warehouse_product_name
    
    class Meta:
        verbose_name = "Warehouse Product"
        verbose_name_plural = "Warehouse Products"
        ordering = ['-warehouse_product_date_added']

class ProductModel(models.Model):
    product_id = models.AutoField(primary_key=True,unique=True)
    product_warehouse_product = models.ForeignKey('WarehouseProductModel',on_delete=models.CASCADE)
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.product_warehouse_product.warehouse_product_name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class SupplierModel(models.Model):
    supplier_id = models.AutoField(primary_key=True,unique=True)
    supplier_companyname = models.CharField(max_length=255)
    supplier_address = models.TextField()
    supplier_mobilenumber = models.CharField(max_length=255)
    supplier_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.supplier_companyname
    
    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

class SaleModel(models.Model):
    sale_id = models.AutoField(primary_key=True,unique=True)
    sale_product = models.ForeignKey('ProductModel',on_delete=models.CASCADE)
    sale_amount = models.FloatField()
    sale_quantity = models.IntegerField()
    sale_customername = models.CharField(max_length=255)
    sale_date = models.DateTimeField(default=datetime.now, blank=True)
    encoded_by = models.ForeignKey('CustomUser',on_delete=models.DO_NOTHING)
    sale_date_added = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self) -> str:
        return self.sale_product.product_warehouse_product.warehouse_product_name
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

class RequestModel(models.Model):
    request_id = models.AutoField(primary_key=True, unique=True)
    request_by = models.ForeignKey('CustomUser',on_delete=models.DO_NOTHING)
    request_order = models.ForeignKey('SaleModel',on_delete=models.CASCADE, null=True, blank=True)
    request_status = models.BooleanField(default=False)
    requested_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.request_by.username
    
    class Meta:
        verbose_name = "Request"
        verbose_name_plural = "Requests"