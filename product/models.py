from django.db import models
from django.contrib.auth import get_user_model
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse_lazy
from slugify import slugify
import datetime

User = get_user_model()
# Create your models here.

class Product_tag(models.Model):
    """
    In this table we can store Tags info
    """
    title = models.CharField('Basliq', max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Size(models.Model):
    """
    In this table we can store Size info
    """
    title = models.CharField('Size', max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Color(models.Model):
    """
    In this table we can store Size info
    """
    title = models.CharField('Color', max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    """
    In this table we can store Category info
    """
    parent_category = models.ForeignKey('self', verbose_name='Parent Category', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_category', blank=True, null=True)

    title = models.CharField('Basliq', max_length=127)

    
    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Product(models.Model):
    """
    In this table we can store Product info
    """
    title = models.CharField('Basliq', max_length=127)
    slug = models.SlugField('Slug')
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    description = models.TextField('Mezmun')
    price = models.DecimalField('Qiymet', max_digits=8, decimal_places=2)
    discount = models.IntegerField('Discount', null=True, default=0)
    is_published = models.BooleanField('Is_published', default=True)
    main_image = models.ImageField('Esas Sekil', upload_to='product_images' , null = True , blank =True)

    #relations
    category = models.ForeignKey(Category, verbose_name='Category',
                                 on_delete=models.CASCADE, db_index=True, related_name='products' , null= True , blank= True)
                                 
    size = models.ManyToManyField(Size, verbose_name='Size', db_index=True, blank=True, related_name='size')

    color = models.ManyToManyField(Color, verbose_name='Color', db_index=True, blank=True, related_name='color')
    
    taglar = models.ManyToManyField(Product_tag, verbose_name='Tags', db_index=True, related_name='product_taglar', blank=True,)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}-{datetime.datetime.now()}')
        return super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('product:single_prod', kwargs={'slug': self.slug})

    @property
    def serialized_data(self):
        return {
            'title': self.title,
            'description': self.description,
            'short_description': self.short_description,
            'slug': self.slug,
            'created_at': str(self.created_at),
        }

    @property
    def set_discount_price(self):
        if self.discount:
            discount_price = self.price - (self.price*self.discount)/100
            return discount_price


class Product_image(models.Model):
    
    image = models.ImageField('Sekil', upload_to='product_images')

    product = models.ForeignKey(Product, verbose_name='Image',
                                on_delete=models.CASCADE, db_index=True, related_name='product_images', null= True, blank= True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Review(models.Model):
    """
    In this table we can store Review info
    """
    title = models.CharField('Basliq', max_length=127)
    rating = models.DecimalField('Rating', max_digits=3, decimal_places=2)
    message = models.TextField('Reyiniz')
    
    #relations
    parent_review = models.ForeignKey('self', verbose_name='Parent Review', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_reviews', blank=True, null=True)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE, db_index=True,
                               related_name='review', null=True, blank=True)

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='review', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


