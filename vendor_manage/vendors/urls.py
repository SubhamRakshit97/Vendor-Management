from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
     # Obtain JWT token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Refresh JWT token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/vendors/', views.VendorListCreate.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view(), name='vendor-detail'),
    path('api/purchase_orders/', views.PurchaseOrderListCreate.as_view(), name='purchaseorder-list-create'),
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroy.as_view(), name='purchaseorder-detail'),
    path('api/vendors/<int:pk>/performance/', views.VendorPerformance.as_view(), name='vendor-performance'),
]
