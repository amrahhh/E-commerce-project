from django import template
from account.forms import SubscriberForm, RegistrationForm, LoginForm

register = template.Library()

@register.simple_tag
def get_subs():
    return SubscriberForm

@register.simple_tag
def get_register():
    return RegistrationForm


@register.simple_tag
def get_login():
    return LoginForm