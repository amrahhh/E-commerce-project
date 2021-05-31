from django import forms
from django.utils.translation import gettext_lazy as _
from product.models import Review
# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'rating',
            'message',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your name')
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': _('Your rating')
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Your review'),
            }),
            
        }


# class ProductForm(forms.ModelForm):
#     # description = forms.CharField(widget=CKEditorWidget())
#     class Meta:
#         model = Product
#         fields = ('title', 'short_description',
#                   'description', 'price', 'category', 'size', 'color','taglar')
#         widgets = {
#             'title': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Title'),
#             }),
#             'short_description': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Short description'),
#             }),
#             'description': CKEditorUploadingWidget(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Description'),
#             }),
#             'price':forms.NumberInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Price'),
#             }),
#             'category': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Category'),
#             }),
#             'size': forms.SelectMultiple(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Size'),
#             }),
#             'taglar': forms.SelectMultiple(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Tags'),
#             }),
#             'author': forms.Select(attrs={
#                 'class': 'form-control',
#                 'placeholder': _('Author')
#             }),
#         }
