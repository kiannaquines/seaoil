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
                )
            }
        )
    )

    list_display = ('username','first_name','last_name','date_joined','is_active',)
    list_filter = ('is_active',)


class AdminWarehouseProduct(admin.ModelAdmin):
    list_display = ("warehouse_product_name","warehouse_product_stock","warehouse_product_status","warehouse_product_supplier","warehouse_product_date_added",)

class AdminProduct(admin.ModelAdmin):
    list_display = ("product_warehouse_product","product_price","product_quantity","product_date_added",)

class AdminSupplier(admin.ModelAdmin):
    list_display = ("supplier_companyname","supplier_mobilenumber","supplier_date_added",)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(ProductModel,AdminProduct)
admin.site.register(SupplierModel,AdminSupplier)
admin.site.register(WarehouseProductModel,AdminWarehouseProduct)
admin.site.register(SaleModel)
admin.site.register(CategoryModel)