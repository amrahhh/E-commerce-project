from django.urls import path
from product.views import *

app_name = 'product'

urlpatterns = [    
    path('product/', ProductListView.as_view(), name='product'),
    path('product/<slug:slug>', ProductDetailView.as_view(), name="single_prod"),
    

]


