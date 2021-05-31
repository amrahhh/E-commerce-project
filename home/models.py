from django.db import models

# Create your models here.

class Alliance(models.Model):
    """
    In this table we can store Alliance companies info
    """
    image = models.ImageField('İmage', upload_to='alliance_images')
    url = models.URLField('URL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.image)
    