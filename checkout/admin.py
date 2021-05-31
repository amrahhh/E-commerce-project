from django.contrib import admin
from checkout.models import (
    Checkout,
    Order,
    OrderItem,
    Wishlist
)

# Register your models here.

@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('title', 'enter', 'company', 'country',)
    list_filter = ('title', 'enter', 'company', 'country',)
    search_fields = ('title', 'enter', 'company', 'country',)


@admin.register(Order)
class Orderdmin(admin.ModelAdmin):
    list_display = ('id', 'transaction_id', )
    list_filter = ('id', 'transaction_id', )
    search_fields = ('id', 'transaction_id', )   

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('quantity',)
    list_filter = ('quantity',)
    search_fields = ('quantity',)

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('author',)
    list_filter = ('author',)
    search_fields = ('author',)