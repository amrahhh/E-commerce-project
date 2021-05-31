from django.db import models

# Create your models here.

class Contact(models.Model):
    """
    In this table we can store user Contact info
    """
    name = models.CharField('Tam adi', max_length=127)
    email = models.EmailField('E-poct', max_length=63)
    message = models.TextField('Mesaj', help_text='Bu qutuya mesajinizi daxil edin')

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
