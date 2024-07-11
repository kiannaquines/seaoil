from django.forms import ModelForm
from app.models import *
from django.contrib.auth.forms import UserCreationForm

class SupplierForm(ModelForm):
    def __init__(self, *args,**kwargs):
        super(SupplierForm,self).__init__(*args,**kwargs)
        self.fields['supplier_companyname'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Company Name'})
        self.fields['supplier_companyname'].label = "Company Name"
        self.fields['supplier_address'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Address','rows':'2'})
        self.fields['supplier_address'].label = "Address"
        self.fields['supplier_mobilenumber'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Mobile No.'})
        self.fields['supplier_mobilenumber'].label = "Mobile Number"

    class Meta:
        model = SupplierModel
        fields = ['supplier_companyname','supplier_address','supplier_mobilenumber']

class CategoryForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(CategoryForm,self).__init__(*args,**kwargs)
        self.fields['category_name'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Category Name'})

    class Meta:
        model = CategoryModel
        fields = ['category_name']

class WarehouseProductForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(WarehouseProductForm,self).__init__(*args,**kwargs)
        self.fields['warehouse_product_name'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Warehouse Product Name'})
        self.fields['warehouse_product_name'].label = "Warehouse Product Name"
        self.fields['warehouse_product_stock'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Stock'})
        self.fields['warehouse_product_stock'].label = "Stock"
        self.fields['warehouse_product_description'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Description','rows':'2'})
        self.fields['warehouse_product_description'].label = "Description"
        self.fields['warehouse_product_category'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['warehouse_product_category'].label = "Category"
        self.fields['warehouse_product_supplier'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['warehouse_product_supplier'].label = "Supplier"
        self.fields['warehouse_product_picture'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['warehouse_product_picture'].label = "Product Image"

    class Meta:
        model = WarehouseProductModel
        fields = ['warehouse_product_name','warehouse_product_stock','warehouse_product_description','warehouse_product_category','warehouse_product_picture','warehouse_product_supplier',]

class ProductForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProductForm,self).__init__(*args,**kwargs)
        self.fields['product_warehouse_product'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['product_warehouse_product'].label = "Warehouse Product"
        self.fields['product_price'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Price'})
        self.fields['product_price'].label = "Price"
        self.fields['product_quantity'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Quantity'})
        self.fields['product_quantity'].label = "Quantity"
    
    class Meta:
        model = ProductModel
        fields = ['product_warehouse_product','product_price','product_quantity']

class SalesForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(SalesForm,self).__init__(*args,**kwargs)
        self.fields['sale_product'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['sale_product'].label = "Product"
        self.fields['sale_quantity'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Quantity'})
        self.fields['sale_quantity'].label = "Quantity"
        self.fields['sale_customername'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Customer Name'})
        self.fields['sale_customername'].label = "Customer Name"
        self.fields['sale_amount'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Amount'})
        self.fields['sale_amount'].label = "Amount"
        self.fields['encoded_by'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['encoded_by'].label = "Encoded By"
    
    class Meta:
        model = SaleModel
        fields = ['sale_product','sale_quantity','sale_customername','sale_amount','encoded_by']
        
class UserRegistrationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserRegistrationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Username'})
        self.fields['username'].label = "Username"
        self.fields['first_name'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'First Name'})
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Last Name'})
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Email'})
        self.fields['email'].label = "Email"
        self.fields['password1'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Password'})
        self.fields['password1'].label = "Password"
        self.fields['password2'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Confirm Password'})
        self.fields['password2'].label = "Confirm Password"
        self.fields['user_address'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Address','rows':'2'})
        self.fields['user_address'].label = "Employee Address"

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','user_address','password1','password2']


class UserUpdateForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(UserUpdateForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Username'})
        self.fields['username'].label = "Username"
        self.fields['first_name'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'First Name'})
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Last Name'})
        self.fields['last_name'].label = "Last Name"
        self.fields['email'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Email'})
        self.fields['email'].label = "Email"
        self.fields['user_address'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Address','rows':'2'})
        self.fields['user_address'].label = "Employee Address"
        self.fields['is_active'].widget.attrs.update({'class':'form-check-input'})
        self.fields['is_staff'].widget.attrs.update({'class':'form-check-input'})
        self.fields['is_superuser'].widget.attrs.update({'class':'form-check-input'})

    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','user_address','is_active','is_staff','is_superuser']
        exclude = ['password1','password2',]


class AttendantSalesForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super(AttendantSalesForm,self).__init__(*args,**kwargs)
        self.fields['sale_product'].widget.attrs.update({'class':'form-control','spellcheck':'false'})
        self.fields['sale_product'].label = "Product"
        self.fields['sale_quantity'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Quantity'})
        self.fields['sale_quantity'].label = "Quantity"
        self.fields['sale_customername'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Customer Name'})
        self.fields['sale_customername'].label = "Customer Name"
        self.fields['sale_amount'].widget.attrs.update({'class':'form-control','spellcheck':'false','placeholder':'Amount'})
        self.fields['sale_amount'].label = "Amount"
    
    class Meta:
        model = SaleModel
        fields = ['sale_product','sale_quantity','sale_customername','sale_amount']









