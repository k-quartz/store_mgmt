from django.shortcuts import render ,get_object_or_404,HttpResponse,redirect
from store import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store import form as Imp_Form
from django.contrib import messages 

# Create your views here.

def index(request):
    return render(request,'store/store.html')

#function for Vendor 
def createVendor(request):
    form=Imp_Form.VendorForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.VendorForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/vendor.html',context)

def vendorreg(request):
    vendorall=models.Vendor.objects.all()
    page=request.GET.get('page',1)

    paginator=Paginator(vendorall,10)
    try:
        vendors=paginator.page(page)
    except PageNotAnInteger:
        vendors=Paginator.page(1)    
    except EmptyPage:
        vendors=Paginator.page(paginator.num_pages)    
    return render(request,'store/vendorreg.html',{"data":vendors})


#Function for Product
def createProduct(request):
    form=Imp_Form.ProductForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.ProductForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/product.html',context)

def productreg(request):
    productall=models.Product.objects.all()
    page=request.GET.get('page',1)

    paginator=Paginator(productall,10)
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=Paginator.page(1)    
    except EmptyPage:
        products=Paginator.page(paginator.num_pages)    
    return render(request,'store/productreg.html',{"data":products})


#Function for PurchaseOrder
def createPurchaseOrder(request):
    form=Imp_Form.PurchaseOrderForm()
    formd=Imp_Form.PurchaseOrderDetailForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.PurchaseOrderForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form,"formd":formd}
    return render(request,'store/purchaseorder.html',context)

def purchaseorderreg(request):
    poall=models.PurchaseOrder.objects.all()
    page=request.GET.get('page',1)

    paginator=Paginator(poall,10)
    try:
        pos=paginator.page(page)
    except PageNotAnInteger:
        pos=Paginator.page(1)    
    except EmptyPage:
        pos=Paginator.page(paginator.num_pages)    
    return render(request,'store/purchaseorderreg.html',{"data":pos})


def updatePurchaseOrder(request,id):
    instance=get_object_or_404(models.PurchaseOrder,id=id)
    form=Imp_Form.PurchaseOrderForm(request.POST or None, instance=instance)
    formd=Imp_Form.PurchaseOrderDetailForm()
    instanced=models.PurchaseOrder_Detail.objects.filter(purchaseorder_id=id)

    page=request.GET.get('page',1)

    paginator=Paginator(instanced,1)
    
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=Paginator.page(1)    
    except EmptyPage:
        products=Paginator.page(paginator.num_pages)

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.PurchaseOrderForm(request.POST)

        if form.is_valid():
            instance=form.save(commit=False)
            form.pono="Akash"
            instance.save()
            
    context={'form':form,"formd":formd,"products":products,"id":id}
    return render(request,'store/purchaseorder.html',context)


#Function for PurchaseorderDetail
def createPurchaseOrderDetail(request):
    form=Imp_Form.PurchaseOrderDetailForm()
    
    print(request.POST["product"])
    if request.method=='POST':
        form=Imp_Form.PurchaseOrderDetailForm(request.POST)
        if form.is_valid():
            pod=models.PurchaseOrder_Detail.objects.filter(product=request.POST["product"])
            if pod.count()>0:
                messages.error(request,"Product already added")
            else:    
                form.save()
        else:
            messages.error(request, "Error")  
    

    id=request.POST["purchaseorder"]
    return redirect(updatePurchaseOrder,id)

def deletePurchaseorderDetail(request,id):
    pod=models.PurchaseOrder_Detail.objects.filter(id=id)
    reccnt=pod.count()
    if reccnt>0:
        pod.delete()
        msg="1"
    else:
        msg="0"

    return HttpResponse(msg)


#Function for Material Inward
def createMaterialInward(request):
    form=Imp_Form.MaterialInwardForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.MaterialInwardForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/inward.html',context)

def inwardreg(request):
    inwardall=models.MaterialInward.objects.all()
    page=request.GET.get('page',1)

    paginator=Paginator(inwardall,10)
    try:
        inwards=paginator.page(page)
    except PageNotAnInteger:
        inwards=Paginator.page(1)    
    except EmptyPage:
        inwards=Paginator.page(paginator.num_pages)    
    return render(request,'store/inwardreg.html',{"data":inwards})


#Function for Material Inward Detail
def createMaterialInwardDetail(request):
    form=Imp_Form.MaterialInward_DetailForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.MaterialInward_DetailForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/inward.html',context)


#Function for Material Issue
def createMaterialIssue(request):
    form=Imp_Form.MaterialIssueForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.MaterialIssueForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/issue.html',context)    


def issuereg(request):
    issueall=models.MaterialIssue.objects.all()
    page=request.GET.get('page',1)

    paginator=Paginator(issueall,10)

    try:
        issues=paginator.page(page)
    except PageNotAnInteger:
        issues=Paginator.page(1)    
    except EmptyPage:
        issues=Paginator.page(paginator.num_pages)    

    return render(request,'store/issuereg.html',{"data":issues})



