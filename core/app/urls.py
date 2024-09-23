from app.views import *
from app.app_views.app_views import *
from app.app_views.generate_report_views import *
from django.urls import path

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
    path('sales/invoice/available',sales_invoice_pagee,name="sales_invoice_pagee"),
    path('user/profile/<int:pk>',user_profile,name="user_profile"),
    path('fetchTotalProductIn/',get_monthly_product_in,name="fetch_product_in"),
    path('fetchTotalSalesMonthly/',get_monthly_yearly_sales,name="fetch_total_sales"),
    path('generateInventoryReport/',generate_inventory_report,name="generate_inventory_report"),
    path('generateSalesReport/',generate_sales_report,name="generateSalesReport"),
    path('manager/',manager_page,name="manager_page"),
    path('manager/warehouse/inventory',inventory_index,name="manager_warehouseproducts_index"),
    path('manager/sales/report',manager_sales_index,name="manager_sales_index"),
    path('attendant/',attendant_page,name="attendant_page"),
    path('attendant/sales/invoice/latest',attendant_sales_invoice_page,name="attendant_sales_invoice_page"),

    # Invoice URL 
    path('attendant/sales/invoice/download/<str:customer>/<str:encoder>/<int:request_id>',generate_sales_invoice,name="generate_sales_invoice"),

    path('attendant/sales/edit/<pk>',AttendantSaleUpdateView.as_view(),name="attendant_sale_edit"),
    path('sales/invoice/download/<str:customer>/<str:encoder>/<int:request_id>',generate_sales_invoice_admin,name="generate_sales_invoice_admin"),


    path("invoice/request",request_list,name="request_list"),
    path("invoice/request/approve",approve_request,name="approve_request"),

    path("attendant/invoice/request/list",attendant_request_list,name="attendant_request_list"),
]
