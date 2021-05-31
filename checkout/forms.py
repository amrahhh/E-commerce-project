from django import forms
from checkout.models import Checkout
from django.utils.translation import gettext_lazy as _

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = (
            'title',
            'enter',
            'phone_number',
            'company',
            'country',
            'state',
            'city',
            'address',
            
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your name')
            }),
            'enter': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter your here')
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Phone here')
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Company name here...')
            }),
            'country': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': _('Country')
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('State')
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Town/City')
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Your address here'),
                'cols': 50
            }),
            
        }