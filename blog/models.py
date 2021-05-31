from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Blog_category(models.Model):
    """
    In this table we can store Blog category info
    """
    title = models.CharField('Basliq', max_length=127)
    
    parent_category = models.ForeignKey('self', verbose_name='Parent Category', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_blog_category', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog_category'
        verbose_name_plural = 'Blog_categories'
        ordering = ('-created_at', )

    def __str__(self):
        return self.title


class Blog_post(models.Model):
    """
    In this table we can store Blogs info
    """
    title = models.CharField('Basliq', max_length=127)
    slug = models.SlugField('Slug', unique=True)
    is_published = models.BooleanField('Is_published')
    author_name = models.CharField('Muellif', max_length=63)
    little_image = models.ImageField('Little image', upload_to = 'product_images', null=True, blank=True)
    image = models.ImageField('Sekil', upload_to='product_images')
    cover_image = models.ImageField('Cover image', upload_to = 'product_images', null=True, blank=True)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    description = models.TextField('Mezmun')
    
    #relation
    category = models.ForeignKey(Blog_category, verbose_name='Category',
                                 on_delete=models.CASCADE, db_index=True, related_name='blog_post' , null =True , blank=True) 
    
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='blog_post', )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    """
    In this table we can store user Comment info
    """
    title = models.CharField('Basliq', max_length=127)
    email = models.EmailField('E-poct', max_length=63, null=True, blank=True)
    message = models.TextField('Reyiniz')

    #relations
    blog_post = models.ForeignKey(Blog_post, verbose_name='Blog', on_delete=models.CASCADE, db_index=True,
                               related_name='comment', )
    parent_comment = models.ForeignKey('self', verbose_name='Parent Comment', on_delete=models.CASCADE, db_index=True,
                                       related_name='sub_comments', blank=True, null=True)

    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE, db_index=True,
                               related_name='comment', )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title

class Tag(models.Model):
    """
    In this table we can store Tags info
    """
    title = models.CharField('Basliq', max_length=127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        