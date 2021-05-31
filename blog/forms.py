from django import forms
from blog.models import Comment
from django.utils.translation import gettext_lazy as _

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'title',
            'email',
            'message',
            'parent_comment'
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Name here')
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': _('Email here')
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': _('Comment here'),
            }),
            'parent_comment': forms.HiddenInput()
            
        }