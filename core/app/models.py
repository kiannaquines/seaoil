from django.db import models
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
    user_address = models.TextField(max_length=255)

    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
     
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class InventoryModel(models.Model):
    inventory_id = models.AutoField(primary_key=True,unique=True)
    inventory_product = models.ForeignKey('ProductModel',on_delete=models.CASCADE)
    inventory_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.inventory_product.product_warehouse_product.warehouse_product_name
    

    class Meta:
        verbose_name = "Inventory"
        verbose_name_plural = "Inventory"

class WarehouseProductModel(models.Model):
    warehouse_product_id = models.AutoField(primary_key=True,unique=True)
    warehouse_product_name = models.CharField(max_length=255)
    warehouse_product_stock = models.IntegerField()
    warehouse_product_description = models.TextField(max_length=355)
    warehouse_product_picture = models.ImageField(upload_to="products/")
    warehouse_product_supplier = models.ForeignKey('SupplierModel',on_delete=models.CASCADE)
    warehouse_product_category = models.ForeignKey('CategoryModel',on_delete=models.DO_NOTHING,null=True,blank=True)
    warehouse_product_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.warehouse_product_name
    
    class Meta:
        verbose_name = "Warehouse Product"
        verbose_name_plural = "Warehouse Products"

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
    sale_customername = models.CharField(max_length=255)
    sale_date = models.DateTimeField(auto_now_add=True)
    encoded_by = models.ForeignKey('CustomUser',on_delete=models.DO_NOTHING)
    sale_date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.sale_product.product_warehouse_product.warehouse_product_name
    
    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

class InvoiceModel(models.Model):
    invoice_id = models.AutoField(primary_key=True,unique=True)
    invoice_sale_product = models.ForeignKey('SaleModel',on_delete=models.CASCADE)
    invoice_date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.invoice_sale_product.sale_product.product_warehouse_product.warehouse_product_name
    
    class Meta:
        verbose_name = "Invoice"



