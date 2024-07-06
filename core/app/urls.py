from django.urls import path
from app.views import *
from app.app_views.app_views import *

urlpatterns = [
	path("",index,name="main_page"),
    path("auth/login/",auth_login,name="auth_login"),
    path("auth/register/",auth_register,name="auth_register"),
    path("auth/logout/",auth_logout,name="auth_logout"),
    path("users/",users_index,name="users_index"),
    path("suppliers/",supplier_index,name="supplier_index"),
    path("inventory/",inventory_index,name="inventory_index"),
    path("category/",category_index,name="category_index"),
    path("product/",products_index,name="products_index"),
    path("sales/",sales_index,name="sales_index"),
    path("warehouseproducts/",warehouseproducts_index,name="warehouseproducts_index"),


    path("supplier/edit/<pk>",SupplierUpdateView.as_view(),name="supplier_edit"),
    path("supplier/confirmation/<pk>",SupplierDeleteView.as_view(),name="supplier_delete")
]
