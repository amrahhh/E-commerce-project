from django import template
from home.models import Alliance

register = template.Library()

@register.simple_tag
def get_alliance():
    return Alliance.objects.all()