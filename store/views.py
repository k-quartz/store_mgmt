from django.shortcuts import render ,get_object_or_404
from store import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store import form as Imp_Form
from django.contrib import messages 

# Create your views here.

def index(request):
    return render(request,'store/store.html')


def createVendor(request):
    form=Imp_Form.VendorForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.VendorForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/vendor.html',context)

def createProduct(request):
    form=Imp_Form.ProductForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.ProductForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/product.html',context)

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

def createPurchaseOrderDetail(request):
    form=Imp_Form.PurchaseOrderDetailForm()
    
    if request.method=='POST':
        print("akash")
        #print(request.POST)
        form=Imp_Form.PurchaseOrderDetailForm(request.POST)
        print(form)
        if form.is_valid():
            print("is valid")
            
            form.save()
        else:
            messages.error(request, "Error")  
            #form.purchaseorder_id=request.POST['purchaseorder_id']

    context={'formd':form}
    return render(request,'store/purchaseorder.html',context)


def createMaterialInward(request):
    form=Imp_Form.MaterialInwardForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.MaterialInwardForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/inward.html',context)


def createMaterialInwardDetail(request):
    form=Imp_Form.MaterialInward_DetailForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.MaterialInward_DetailForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/inward.html',context)

def createMaterialIssue(request):
    form=Imp_Form.MaterialIssueForm()

    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.MaterialIssueForm(request.POST)

        if form.is_valid():
            form.save()

    context={'form':form}
    return render(request,'store/issue.html',context)    

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


def updatePurchaseOrder(request,id):
    instance=get_object_or_404(models.PurchaseOrder,id=id)
    form=Imp_Form.PurchaseOrderForm(request.POST or None, instance=instance)
    formd=Imp_Form.PurchaseOrderDetailForm()
    instanced=models.PurchaseOrder_Detail.objects.filter(purchaseorder_id=id)
    if request.method=='POST':
        print(request.POST)
        form=Imp_Form.PurchaseOrderForm(request.POST)

        if form.is_valid():
            form.save()
    
    context={'form':form,"formd":formd,"products":instanced,"id":id}
    return render(request,'store/purchaseorder.html',context)