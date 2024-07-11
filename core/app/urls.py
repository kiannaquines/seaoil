from django.urls import path
from app.views import *
from app.app_views.app_views import *
from app.app_views.generate_report_views import *

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
    path("supplier/confirmation/<pk>",SupplierDeleteView.as_view(),name="supplier_delete"),
    path("user/edit/<pk>",UserUpdateView.as_view(),name="user_edit"),
    path("user/confirmation/<pk>",DeleteUserView.as_view(),name="user_delete"),
    path("category/edit/<pk>",CategoryEditView.as_view(),name="category_edit"),
    path("category/confirmation/<pk>",CategoryDeleteView.as_view(),name="category_delete"),
    path("warehouseproduct/edit/<pk>",WarehouseProductUpdateView.as_view(),name="warehouseproduct_edit"),
    path("warehouseproduct/confirmation/<pk>",WarehouseProductDeleteView.as_view(),name="warehouseproduct_delete"),
    path("product/edit/<pk>",ProductUpdateView.as_view(),name="product_edit"),
    path("product/confirmation/<pk>",ProductDeleteView.as_view(),name="product_delete"),
    path("sale/edit/<pk>",SaleUpdateView.as_view(),name="sale_edit"),
    path("sale/confirmation/<pk>",SaleDeleteView.as_view(),name="sale_delete"),
    path('user/profile/<int:pk>',user_profile,name="user_profile"),
    path('fetchTotalProductIn/',get_monthly_product_in,name="fetch_product_in"),
    path('fetchTotalSalesMonthly/',get_monthly_yearly_sales,name="fetch_total_sales"),

    path('generateInventoryReport/',generate_inventory_report,name="generate_inventory_report"),
    path('generateSalesReport/',generate_sales_report,name="generateSalesReport"),


    path('manager/',manager_page,name="manager_page"),
    path('attendant/',attendant_page,name="attendant_page"),
    path('attendant/sales/invoice/latest',attendant_sales_invoice_page,name="attendant_sales_invoice_page"),
    path('attendant/sales/invoice/all',all_attendant_sales_invoice_page,name="all_attendant_sales_invoice_page"),
    path('attendant/sales/invoice/download/<str:name>/<str:encoder>/<str:invoice_type>',generate_sales_invoice,name="generate_sales_invoice"),
]
