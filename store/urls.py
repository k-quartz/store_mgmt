from django.urls import path
from store import views
#from store.views import CreateMaterialInward,CreateVendor

urlpatterns = [
    path('', views.index,name='store-index'),
    path('vendor/add/',views.createVendor,name='add-vendor'),
    path('product/add/',views.createProduct,name='add-product'),
    path('po/add/',views.createPurchaseOrder,name='add-po'),
    path('pod/add/',views.createPurchaseOrderDetail,name='add-pod'),
    path('inward/add/',views.createMaterialInward,name='add-inward'),
    path('issue/add/',views.createMaterialIssue,name='add-issue'),

    path('vendor/',views.vendorreg,name='vendorreg'),
    path('product/',views.productreg,name='productreg'),
    path('po/',views.purchaseorderreg,name='poreg'),
    path('inward/',views.inwardreg,name='inwardreg'),
    path('issue/',views.issuereg,name='issuereg'),


    path('vendor/update/<id>',views.inwardreg,name='update-vendor'),
    path('product/update/<id>',views.inwardreg,name='update-product'),
    path('po/update/<id>',views.updatePurchaseOrder,name='update-po'),
    path('inward/update/<id>',views.inwardreg,name='update-inward'),
    path('issue/update/<id>',views.issuereg,name='update-issue'),

    path('pod/delete/<id>',views.deletePurchaseorderDetail,name="delete-pod"),
]
