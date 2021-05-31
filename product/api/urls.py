from django.urls import path
from product.api.views import ProductAPIView, ProductDetailAPIView, CategoryAPIView, CategoryDetailAPIView

urlpatterns = [
    path('product/', ProductAPIView.as_view(), name='product_api'),
    path('product/<int:pk>', ProductDetailAPIView.as_view(), name='product_detail_api'),
    path('category/', CategoryAPIView.as_view(), name='category_api'),
    path('category/<int:pk>', CategoryDetailAPIView.as_view(), name='category_detail_api'),


]   