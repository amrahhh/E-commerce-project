from django.urls import path
from checkout.views import *

app_name = 'checkout'

urlpatterns = [    
    path('checkout/', checkout, name='checkout'),
    path('complete/', completed, name='complete'),
    path('wishlist/', wishlist, name='wishlist'),
    path('error/', error, name='error'),
    path('cart/', cart, name='cart'),
]