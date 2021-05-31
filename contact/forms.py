from django import forms
from contact.models import Contact
from django.utils.translation import gettext_lazy as _
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'name',
            'email',
            'message'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter your name...')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Enter your email...')
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Enter your message...',)
            })
            
        }