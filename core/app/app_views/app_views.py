from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DeleteView, UpdateView
from app.decorators import *
from django.utils.decorators import method_decorator

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
def supplier_index(request):
    suppliers = SupplierModel.objects.all()
    supplier_form = SupplierForm()

    context = {
        'suppliers':suppliers,
        'form': supplier_form,
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
    context = {
        'inventories':inventories,
    }

    return render(request,"inventory.html",context)

# DONE
@login_required(login_url="/auth/login/")
@check_user_permission_based_on_user_type
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
    


def manager_page(request):
    return render(request, "manager/manager.html")

def attendant_page(request):
    return render(request, "attendant/attendant.html")











