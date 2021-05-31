from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import (
    Product,
    Category,
    Review,
    Size,
    Color,
    Product_tag, 
    Product_image
)
# Register your models here.


class Product_imageInline(admin.TabularInline):
    model = Product_image


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [Product_imageInline,]
    list_display = ('title', 'category', 'price',)
    list_filter = ('title', 'category', 'price',)
    search_fields = ('title', 'category', 'price',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'message',)
    list_filter = ('title', 'rating', 'message',)
    search_fields = ('title', 'rating', 'message',)
  
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', )
    search_fields = ('title',) 

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', )
    search_fields = ('title',) 

@admin.register(Product_tag)
class Product_tagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title', )
    search_fields = ('title',) 


class CategoryAdmin(TranslationAdmin):
    search_fields = ('title',)
    list_display = ('id', 'title', 'created_at')

admin.site.register(Category, CategoryAdmin)