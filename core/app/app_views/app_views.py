from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, UpdateView
from django.template.loader import render_to_string
from django.http import JsonResponse

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

# DONE
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
class SupplierDeleteView(DeleteView):
    model = SupplierModel
    pk_url_kwarg = "pk"
    template_name = "forms/supplier_delete_form.html"
    success_url = '/suppliers/'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'You have successfully removed supplier information, thank you!',extra_tags="delete_success")
        return response

# DONE
@login_required(login_url="/auth/login/")
def users_index(request):
    users = CustomUser.objects.all()
    user_form = UserRegistrationForm()

    context = {
        'users': users,
        'register_form': user_form,
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

class UserUpdateView(UpdateView):
    pass

class DeleteUserView(DeleteView):
    pass


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


class CategoryEditView(UpdateView):
    pass

class CategoryDeleteView(DeleteView):
    pass

@login_required(login_url="/auth/login/")
def inventory_index(request):
    inventories = WarehouseProductModel.objects.all()
    context = {
        'inventories':inventories,
    }

    return render(request,"inventory.html",context)

@login_required(login_url="/auth/login/")
def products_index(request):
    products = ProductModel.objects.all()
    products_form = ProductForm()

    context = {
        'products':products,
        'products_form':products_form,
    }

    if request.method == "POST":
        products_form = ProductForm(request.POST)
        if products_form.is_valid():
            products_form.save()
            messages.success(request,"You have added new product, thank you!",extra_tags="add_success")
            return HttpResponseRedirect("/product/")
        else:
            messages.error(request,"Something went wrong, please try again.",extra_tags="some_error")
            return HttpResponseRedirect("/product/")

    return render(request,"products.html",context)

class ProductUpdateView(UpdateView):
    pass

class ProductDeleteView(DeleteView):
    pass

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
    sale_form = SalesForm()

    context = {
        'sales':sales,
        'form_sales':sale_form,
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