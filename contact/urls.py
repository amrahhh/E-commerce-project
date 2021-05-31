from django.urls import path
from contact.views import *

app_name = 'contact'

urlpatterns = [    
    path('contact/', ContactView.as_view(), name="contact"), 
    path('contact-us/', contact_us, name='contact_us'),
]