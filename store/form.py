from django import forms
from store import models

class DateInput(forms.DateInput):
    input_type='date'

class VendorForm(forms.ModelForm):
    class Meta:
        model=models.Vendor
        fields='__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields='__all__'        \

class PurchaseOrderForm(forms.ModelForm):
    vendor=forms.ModelChoiceField(queryset=models.Vendor.objects.all(),empty_label="Select Vendor")
    podate=forms.DateField(widget=DateInput)
    class Meta:
        model=models.PurchaseOrder
        fields='__all__'

class PurchaseOrderDetailForm(forms.ModelForm):
    product=forms.ModelChoiceField(queryset=models.Product.objects.all(),empty_label="Select Product")
    class Meta:
        model=models.PurchaseOrder_Detail
        fields=['product','poqty','rate']        

class MaterialInwardForm(forms.ModelForm):
    vendor=forms.ModelChoiceField(queryset=models.Vendor.objects.all(),empty_label="Select Vendor")
    inwarddate=forms.DateField(widget=DateInput)
    class Meta:
        model=models.MaterialInward
        fields='__all__'

class MaterialInward_DetailForm(forms.ModelForm):
    class Meta:
        model=models.MaterialInward_Detail
        fields='__all__'                

class MaterialIssueForm(forms.ModelForm):
    vendor=forms.ModelChoiceField(queryset=models.Vendor.objects.all(),empty_label="Select Vendor")
    issuedate=forms.DateField(widget=DateInput)
    class Meta:
        model=models.MaterialIssue
        fields='__all__'