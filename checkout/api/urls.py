from django.urls import path
from checkout.api.views import OrderItemAPIView, OrderItemDetailAPIView

urlpatterns = [
    path('order-item/', OrderItemAPIView.as_view(), name='order_item_api'),
    path('order-item/<int:pk>', OrderItemDetailAPIView.as_view(), name='order_item_detail_api'),
]   