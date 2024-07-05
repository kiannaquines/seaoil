from django.forms import ModelForm
from app.models import *


class SupplierForm(ModelForm):
    def __init__(self, *args,**kwargs):
        super(SupplierForm,self).init(*args,**kwargs)
        self.fields['supplier_companyname'].widget.attrs.update({'class':'form-control'})
        self.fields['supplier_companyname'].label = "Company Name"

    class Meta:
        model = SupplierModel
        fields = ['supplier_companyname','supplier_address','supplier_mobilenumber']