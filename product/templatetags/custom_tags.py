from django.template import Library
from product.models import Category

register = Library()

@register.simple_tag
def get_product_categories():
    return Category.objects.all()