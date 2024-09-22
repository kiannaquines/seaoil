from django.contrib import admin
from app.models import *
from django.contrib.auth.admin import UserAdmin as OriginalAdmin

class CustomUserAdmin(OriginalAdmin):
    fieldsets = (
        *OriginalAdmin.fieldsets,
        (
            'User Accounts Information',
            {
                'fields': (
                    'user_address',
                    'user_type',
                )
            }
        )
    )

    list_display = ('username','first_name','last_name','user_type','date_joined','is_active',)
    list_filter = ('is_active',)
    list_editable = ["user_type",]


class AdminWarehouseProduct(admin.ModelAdmin):
    list_display = ("warehouse_product_name","warehouse_product_stock","warehouse_product_status","warehouse_product_supplier","warehouse_product_date_added",)
    list_editable = ["warehouse_product_stock","warehouse_product_status",]
    fields = ("warehouse_product_name","warehouse_product_stock","warehouse_product_description","warehouse_product_picture","warehouse_product_supplier","warehouse_product_category","warehouse_product_status","warehouse_product_date_added")

class AdminProduct(admin.ModelAdmin):
    list_display = ("product_warehouse_product","product_price","product_quantity","product_date_added",)
    list_filter = ("product_warehouse_product","product_date_added",)
    ordering = ["-product_date_added"]
    list_per_page = 10
    list_display_links = ("product_warehouse_product",)
    date_hierarchy = "product_date_added"
    list_editable = ["product_price","product_quantity"]


class AdminSupplier(admin.ModelAdmin):
    list_display = ("supplier_companyname","supplier_mobilenumber","supplier_date_added",)


admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(ProductModel,AdminProduct)
admin.site.register(SupplierModel,AdminSupplier)
admin.site.register(WarehouseProductModel,AdminWarehouseProduct)
admin.site.register(SaleModel)
admin.site.register(InvoiceRequestModel)
admin.site.register(CategoryModel)