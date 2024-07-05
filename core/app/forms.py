from django.forms import ModelForm
from app.models import *


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
