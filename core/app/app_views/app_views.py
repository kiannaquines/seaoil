from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages

# DONE
@login_required(login_url="/auth/login/")
def supplier_index(request):
    suppliers = SupplierModel.objects.all()
    supplier_form = SupplierForm()

    context = {
        'suppliers':suppliers,
        'supplier_form': supplier_form,
    }

    if request.method == "POST":
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            supplier_form.save()
            messages.success(request,"You have added new supplier, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/suppliers/")        
        
    return render(request,"supplier.html",context)

@login_required(login_url="/auth/login/")
def users_index(request):
    users = CustomUser.objects.all()
    context = {
        'users': users
    }

    if request.method == "POST":
        pass

    return render(request,"users.html",context)

# DONE
@login_required(login_url="/auth/login/")
def category_index(request):
    categories = CategoryModel.objects.all()
    category_form = CategoryForm()
    context = {
        'categories':categories,
        'category_form': category_form,
    }

    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"You have added new category, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/category/")

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
    warehouseproducts_form = WarehouseProductForm()

    context = {
        'warehouseproducts':warehouseproducts,
        'warehouseproducts_form': warehouseproducts_form,
    }

    if request.method == "POST":
        warehouseproducts_form = WarehouseProductForm(request.POST,request.FILES)
        if warehouseproducts_form.is_valid():
            warehouseproducts_form.save()
            messages.success(request,"You have added new warehouse product, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/warehouseproducts/")
        else:
            messages.error(request,"Something went wrong, please try again.",extra_tags="some_error")
            return HttpResponseRedirect("/warehouseproducts/")

    return render(request,"warehouseproducts.html",context)

@login_required(login_url="/auth/login/")
def sales_index(request):
    sales = SaleModel.objects.all()

    context = {
        'sales':sales,
    }

    return render(request,"sales.html",context)