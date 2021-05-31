from celery import shared_task
from account.models import Subscriber
from product.models import Product
from django.db.models import Count
from shellshop import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def send_emails_to_subscribers():
    subject = ('Latest popular products for you.')
    subscribers = Subscriber.objects.values_list('email', flat=True)
    previous_week = datetime.date.today() - datetime.timedelta(days=7)
    today = datetime.date.today()
    products = Product.objects.filter(is_published=True, created_at__range=[previous_week, today]).annotate(Count('review__message')).order_by('-review__message__count')[:3]
    print(products)

    context = {
        'products': products,
        'SITE_ADDRESS': settings.SITE_ADDRESS,
    }

    body = render_to_string('emails/email-subscribers.html', context)
    mail = EmailMessage(subject, to=subscribers, from_email=settings.EMAIL_HOST_USER, body=body)
    mail.content_subtype = 'html'
    mail.send()


@shared_task
def send_emails_to_last_login30():
    subject = ('Latest popular products for you.')
    last_login30days = datetime.date.today() - datetime.timedelta(days=30)
    users = User.objects.filter(last_login__lt=last_login30days).values_list('email', flat=True)
    previous_week = datetime.date.today() - datetime.timedelta(days=30)
    today = datetime.date.today()
    products = Product.objects.filter(is_published=True, created_at__range=[previous_week, today]).annotate(Count('review__message')).order_by('-review__message__count')[:5]
    
    context = {
        'products': products,
        'SITE_ADDRESS': settings.SITE_ADDRESS,
    }
    
    body = render_to_string('emails/email-subscribers.html', context)
    mail = EmailMessage(subject, to=users,
                        from_email=settings.EMAIL_HOST_USER, body=body)
    mail.content_subtype = 'html'
    mail.send()
