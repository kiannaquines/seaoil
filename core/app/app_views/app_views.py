from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/auth/login/")
def supplier_index(request):
    return render(request,"supplier.html")

@login_required(login_url="/auth/login/")
def category_index(request):
    return render(request,"category.html")

@login_required(login_url="/auth/login/")
def inventory_index(request):
    return render(request,"inventory.html")

@login_required(login_url="/auth/login/")
def invoice_index(request):
    return render(request,"invoice.html")

@login_required(login_url="/auth/login/")
def products_index(request):
    return render(request,"products.html")

@login_required(login_url="/auth/login/")
def warehouseproducts_index(request):
    return render(request,"warehouseproucts.html")