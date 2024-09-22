from app.models import *
from app.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from app.decorators import *
from django.utils import timezone
from core.settings import MINIMUM
from django.db.models import Sum,F,Count
from django.db.models.functions import Lower
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def supplier_index(request):
    suppliers = SupplierModel.objects.all()
    supplier_form = SupplierForm()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()


    context = {
        'suppliers':suppliers,
        'form': supplier_form,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    if request.method == "POST":
        supplier_form = SupplierForm(request.POST)
        if supplier_form.is_valid():
            supplier_form.save()
            messages.success(request,"You have added new supplier, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/suppliers/")        
        
    return render(request,"supplier.html",context)

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class SupplierUpdateView(UpdateView):
    form_class = SupplierForm
    model = SupplierModel
    pk_url_kwarg = "pk"
    template_name = "forms/supplier_edit_form.html"
    success_url = '/suppliers/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated supplier information, thank you!',extra_tags="edit_success")
        return response

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')    
class SupplierDeleteView(DeleteView):
    model = SupplierModel
    pk_url_kwarg = "pk"
    template_name = "forms/delete_form.html"
    success_url = '/suppliers/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed supplier information, thank you!',extra_tags="delete_success")
        return response

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def users_index(request):
    users = CustomUser.objects.all()
    user_form = UserRegistrationForm()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()

    context = {
        'users': users,
        'register_form': user_form,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,"You have added new user, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/users/")
        else:
            for user_error in user_form.errors:
                for error in user_form.errors[user_error]:
                    messages.error(request,error,extra_tags="some_error")
            return HttpResponseRedirect("/users/")
        
    return render(request,"users.html",context)

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class UserUpdateView(UpdateView):
    model = CustomUser
    pk_url_kwarg = "pk"
    form_class = UserUpdateForm
    template_name = "forms/user_edit_form.html"
    success_url = "/users/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated user information, thank you!',extra_tags="edit_success")
        return response

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class DeleteUserView(DeleteView):
    model = CustomUser
    success_url = '/users/'
    template_name = "forms/delete_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed user information, thank you!',extra_tags="delete_success")
        return response


# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def category_index(request):
    categories = CategoryModel.objects.all()
    category_form = CategoryForm()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()

    context = {
        'categories':categories,
        'category_form': category_form,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request,"You have added new category, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/category/")

    return render(request,"category.html",context)

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class CategoryEditView(UpdateView):
    model = CategoryModel
    pk_url_kwarg = "pk"
    form_class = CategoryForm
    success_url = "/category/"
    template_name = "forms/category_edit_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated category information, thank you!',extra_tags="edit_success")
        return response

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = CategoryModel
    pk_url_kwarg = "pk"
    success_url = "/category/"
    template_name = "forms/delete_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed category information, thank you!',extra_tags="delete_success")
        return response

@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def inventory_index(request):
    inventories = WarehouseProductModel.objects.all()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()

    context = {
        'inventories':inventories,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    return render(request,"inventory.html",context)

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def products_index(request):
    products = ProductModel.objects.all()
    products_form = ProductForm()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()


    context = {
        'products':products,
        'products_form':products_form,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    if request.method == "POST":
        products_form = ProductForm(request.POST)
        if products_form.is_valid():
            products_form.save()

            warehouse_product = products_form.cleaned_data['product_warehouse_product'].warehouse_product_id
            
            WarehouseProductModel.objects.filter(
                warehouse_product_id=warehouse_product
            ).update(
                warehouse_product_stock=F('warehouse_product_stock') - products_form.cleaned_data['product_quantity']
            )

            messages.success(
                request,
                "You have pulled out stock product from warehouse, thank you!",
                extra_tags="add_success"
            )

            return HttpResponseRedirect("/product/")
        else:

            messages.error(
                request,
                "Something went wrong, please try again.",
                extra_tags="some_error"
            )

            return HttpResponseRedirect("/product/")

    return render(request,"products.html",context)

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class ProductUpdateView(UpdateView):
    model = ProductModel
    form_class = ProductForm
    pk_url_kwarg = "pk"
    template_name = "forms/product_edit_form.html"
    success_url = "/product/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated product information, thank you!',extra_tags="edit_success")
        return response

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class ProductDeleteView(DeleteView):
    model = ProductModel
    pk_url_kwarg = "pk"
    success_url = '/product/'
    template_name = "forms/delete_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed product information, thank you!',extra_tags="delete_success")
        return response

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def warehouseproducts_index(request):
    warehouseproducts = WarehouseProductModel.objects.all()
    warehouseproducts_form = WarehouseProductForm()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()


    context = {
        'warehouseproducts':warehouseproducts,
        'warehouseproducts_form': warehouseproducts_form,
        'warehouse_product_stock_check': warehouse_product_stock_check,
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

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class WarehouseProductUpdateView(UpdateView):
    model = WarehouseProductModel
    form_class = WarehouseProductForm
    pk_url_kwarg = "pk"
    template_name = "forms/warehouseproduct_edit_form.html"
    success_url = "/warehouseproducts/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated warehouse product information, thank you!',extra_tags="edit_success")
        return response

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class WarehouseProductDeleteView(DeleteView):
    model = WarehouseProductModel
    pk_url_kwarg = "pk"
    template_name = "forms/delete_form.html"
    success_url = "/warehouseproducts/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed warehouse product information, thank you!',extra_tags="delete_success")
        return response

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def sales_index(request):
    sales = SaleModel.objects.all()
    sale_form = SalesForm()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()

    context = {
        'sales':sales,
        'form_sales':sale_form,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    if request.method == "POST":
        sale_form = SalesForm(request.POST)
        if sale_form.is_valid():
            sale_form.save()
            messages.success(request,"You have added new sale, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/sales/")
        else:
            messages.error(request,"Something went wrong, please try again.",extra_tags="some_error")
            return HttpResponseRedirect("/sales/")
        
    return render(request,"sales.html",context)

@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def manager_sales_index(request):
    sales = SaleModel.objects.all()
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()

    context = {
        'sales':sales,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }
        
    return render(request,"manager/sales.html",context)


# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class SaleUpdateView(UpdateView):
    model = SaleModel
    form_class = SalesForm
    pk_url_kwarg = "pk"
    template_name = "forms/sale_edit_form.html"
    success_url = "/sales/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated sale information, thank you!',extra_tags="edit_success")
        return response

# DONE
@method_decorator(check_if_logged_in,name='dispatch')
@method_decorator(check_user_permission_based_on_user_type, name='dispatch')
class SaleDeleteView(DeleteView):
    model = SaleModel
    pk_url_kwarg = "pk"
    success_url = "/sales/"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed sale information, thank you!',extra_tags="delete_success")
        return response
    
@login_required(login_url="/auth/login/")
def manager_page(request):
    today_date = timezone.now().date()
    last_week = today_date - timezone.timedelta(days=7)
    # total_sale = SaleModel.objects.aggregate(sale=Sum('sale_amount'))
    warehouse_product_count = WarehouseProductModel.objects.all().count()
    product_count_today = WarehouseProductModel.objects.filter(warehouse_product_date_added__date=today_date).all().count()
    latest_transactions = SaleModel.objects.all().order_by('-sale_date_added')[:7]
    last_weeks_data = WarehouseProductModel.objects.filter(warehouse_product_date_added__range=[last_week, today_date]).count()

    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()


    context = {
        # 'total_sale':total_sale,
        'total_products_count':warehouse_product_count,
        'todays_product_count':product_count_today,
        'warehouseproduct_count':warehouse_product_count,
        'latest_transactions':latest_transactions,
        'last_weeks_data_count':last_weeks_data,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }

    return render(request, "manager/manager.html",context)


@login_required(login_url="/auth/login/")
def attendant_page(request):
    sales_form = AttendantSalesForm()
    sales = SaleModel.objects.filter(encoded_by=CustomUser.objects.get(id=request.user.id)).all().order_by('-sale_date_added')

    context = {
        'form':sales_form,
        'sales': sales,
    }

    if request.method == "POST":
        sales_form = AttendantSalesForm(request.POST)
        sales_quantity = int(request.POST.get('sale_quantity'))

        if sales_form.is_valid():

            sale = sales_form.save(commit=False)
            sale.encoded_by = request.user
            sale.save()

            current_sold_obj = ProductModel.objects.get(product_id=request.POST.get('sale_product'))
            current_sold_obj.product_sold = current_sold_obj.product_sold + sales_quantity
            current_sold_obj.product_quantity = current_sold_obj.product_quantity - sales_quantity
            current_sold_obj.save()

            messages.success(request,"You have added new sale, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/attendant/")
        else:
            print(sales_form.errors)
            messages.error(request,"Something went wrong, please try again.",extra_tags="some_error")
            return HttpResponseRedirect("/attendant/")

    return render(request, "attendant/attendant.html",context)

@login_required(login_url="/auth/login/")
def attendant_sales_invoice_page(request):

    today = timezone.now().date()

    sales_invoice = SaleModel.objects.filter(
        sale_date_added__date=today,
        encoded_by=request.user
    )
    
    context = {
        'sales_invoice': sales_invoice,
        'type': 'latest',
    }

    return render(request, "attendant/invoice_list.html",context)

@method_decorator(check_if_logged_in,name='dispatch')
class AttendantSaleUpdateView(UpdateView):
    model = SaleModel
    form_class = AttendantSalesForm
    pk_url_kwarg = "pk"
    template_name = "forms/sale_edit_form.html"
    success_url = reverse_lazy('attendant_page')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully updated sale information, thank you!',extra_tags="edit_success")
        return response


@login_required(login_url="/auth/login/")
def sales_invoice_pagee(request):

    sales_invoice = InvoiceRequestModel.objects.all()
    
    warehouse_product_stock_check = WarehouseProductModel.objects.filter(warehouse_product_stock__lt=MINIMUM).all()

    context = {
        'sales_invoice': sales_invoice,
        'warehouse_product_stock_check': warehouse_product_stock_check,
    }
    

    return render(request, "sales_invoice.html",context)


