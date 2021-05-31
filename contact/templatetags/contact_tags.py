from django import template
from contact.forms import ContactForm

register = template.Library()

@register.simple_tag
def get_form():
    return ContactForm