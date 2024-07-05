from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import *

@login_required(login_url="/auth/login/")
def supplier_index(request):
    suppliers = SupplierModel.objects.all()

    context = {
        'suppliers':suppliers,
    }

    return render(request,"supplier.html",context)

@login_required(login_url="/auth/login/")
def users_index(request):
    users = CustomUser.objects.all()

    context = {
        'users': users
    }

    return render(request,"users.html",context)


@login_required(login_url="/auth/login/")
def category_index(request):
    categories = CategoryModel.objects.all()
    context = {
        'categories':categories,
    }

    return render(request,"category.html",context)

@login_required(login_url="/auth/login/")
def inventory_index(request):
    inventories = InventoryModel.objects.all()
    context = {
        'inventories':inventories,
    }

    return render(request,"inventory.html",context)

@login_required(login_url="/auth/login/")
def invoice_index(request):
    invoices = InvoiceModel.objects.all()
    
    context = {
        'invoices':invoices,
    }

    return render(request,"invoice.html",context)

@login_required(login_url="/auth/login/")
def products_index(request):
    products = ProductModel.objects.all()

    context = {
        'products':products,
    }

    return render(request,"products.html",context)

@login_required(login_url="/auth/login/")
def warehouseproducts_index(request):
    warehouseproducts = WarehouseProductModel.objects.all()

    context = {
        'warehouseproducts':warehouseproducts,
    }

    return render(request,"warehouseproducts.html",context)

@login_required(login_url="/auth/login/")
def sales_index(request):
    sales = SaleModel.objects.all()

    context = {
        'sales':sales,
    }

    return render(request,"sales.html",context)