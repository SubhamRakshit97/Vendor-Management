from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', views.PurchaseOrderListCreate.as_view(), name='purchaseorder-list-create'),
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchaseorder-detail'),
    path('api/vendors/<int:pk>/performance/', views.VendorPerformance.as_view(), name='vendor-performance'),
]
