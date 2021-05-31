from django.shortcuts import render, redirect
from checkout.models import *
from django.contrib import messages
from checkout.forms import CheckoutForm
from django.http import JsonResponse
from checkout.models import Order
from product.models import Product
import json
# Create your views here.

def checkout(request):
    check = Checkout.objects.all()
    form = CheckoutForm()
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        print(request.POST , form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, 'Müraciətiniz uğurla təsdiqləndi.')
            return redirect('/')

    context = {
        'check': check,
        'form': form
    }
    return render(request, 'checkout.html', context)

def completed(request):
    return render(request, 'order-complete.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def error(request):
    return render(request, 'error-404.html')

def cart(request):
    return render(request, 'cart.html')