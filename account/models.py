from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Subscriber(models.Model):
    """
    In this table we can store Subscriber info
    """
    email = models.EmailField('E-poct', max_length=63)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField('Phone number', max_length=127)
    image = models.ImageField('Image', upload_to='profile_pictures', null=True, blank=True)
    bio = models.TextField('Bio', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def profile_picture(self):
        if self.image:
            return self.image
        return 'https://www.pngfind.com/pngs/m/470-4703547_icon-user-icon-hd-png-download.png'
