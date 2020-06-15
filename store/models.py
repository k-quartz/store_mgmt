from django.db import models

# Create your models here.

class Product(models.Model):
    productname=models.CharField(max_length=255)
    specification=models.CharField(max_length=255)
    minStock=models.FloatField()
    reOrderPoint=models.FloatField()
    minOrderQty=models.FloatField()
    #productImage=models.ImageField()

    def __str__(self):
        return self.productname

    class Meta:
        managed=True
        db_table='product'

class Vendor(models.Model):
    vendorname=models.CharField(max_length=255)
    vend_address=models.TextField()
    gstno=models.CharField(max_length=25)

    def __str__(self):
        return self.vendorname

    class Meta:
        managed=True
        db_table='vendor'

class MaterialIssue(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    issuedate=models.DateField(auto_now_add=True)

    class Meta:
        managed=True
        db_table='materialissue'


class PurchaseOrder(models.Model):
    pono=models.CharField(max_length=100)
    podate=models.DateField()
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    remarks=models.TextField()

    class Meta:
        managed=True
        db_table='purchaseorder'


class PurchaseOrder_Detail(models.Model):
    purchaseorder=models.ForeignKey(PurchaseOrder,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)        
    poqty=models.FloatField()
    rate=models.FloatField()
    cancleqty=models.FloatField(default=0)
    pending_qty=models.FloatField(default=0)

    class Meta:
        managed=True
        db_table='purchaseorder_detail'


class MaterialInward(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    inwarddate=models.DateField(auto_now_add=False)
    billno=models.CharField(max_length=30)

    class Meta:
        managed=True
        db_table='materialinward'

class MaterialInward_Detail(models.Model):
    materialinward=models.ForeignKey(MaterialInward,on_delete=models.CASCADE)
    purchasedetail=models.ForeignKey(PurchaseOrder_Detail,on_delete=models.CASCADE, default=0)
    inwardqty=models.FloatField()
    issuedqty=models.FloatField()

    class Meta:
        managed=True
        db_table='materialinward_detail'
