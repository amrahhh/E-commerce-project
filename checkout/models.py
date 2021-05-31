from django.db import models
from django_countries.fields import CountryField
from product.models import Product
from decimal import Decimal
from django.db.models import F, Sum
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Checkout(models.Model):
    """
    In this table we can store Checkout info
    """
    title = models.CharField('Name', max_length=127)
    enter = models.CharField('Enter your here', max_length=127)
    phone_number = models.CharField('Phone number', max_length=127)
    company = models.CharField('Company name', max_length=127)
    country = CountryField('Country')
    state = models.CharField('State', max_length=127)
    city = models.CharField('City', max_length=127)
    address = models.CharField('Address', max_length=127)
    note = models.CharField('Note', max_length=127, blank=True, null=True)

    # relation
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='product', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    """
    In this table we can store Order info
    """
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='order_product', null=True, blank=True)

    complete = models.BooleanField(default=False)

    transaction_id = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    """
    In this table we can store Order item info
    """
    # order = models.ForeignKey(Order, verbose_name='Order', on_delete=models.CASCADE, db_index=True,
    #                            related_name='order', )

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='product_order', null=True, blank=True)

    product = models.ForeignKey(Product, verbose_name='Product item', on_delete=models.CASCADE, db_index=True,
                                related_name='product_order', )

    # checkout = models.ForeignKey(Checkout, verbose_name='Checkout', on_delete=models.CASCADE, db_index=True,
    #                            related_name='order', )

    quantity = models.IntegerField(default=1, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.quantity)

    @property
    def get_total_price(self):
        return self.product.set_discount_price * self.quantity


class Wishlist(models.Model):
    """
    In this table we can store Wishlist info
    """
    author = models.ForeignKey(User, verbose_name='Wish author', on_delete=models.CASCADE, db_index=True,
                               related_name='wish_prod', )

    product_item = models.ForeignKey(Product, verbose_name='Wish product item', on_delete=models.CASCADE, db_index=True,
                                     related_name='wish_prod', )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
