from django.contrib import admin
from blog.models import (
    Blog_post,
    Comment, 
    Tag,
    Blog_category,
)

# Register your models here.

@admin.register(Blog_post)
class Blog_postAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author_name', 'image', 'short_description',)
    list_filter = ('title', 'author_name', 'image', 'short_description',)
    search_fields = ('title', 'author_name', 'image', 'short_description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'message',)
    list_filter = ('title', 'message',)
    search_fields = ('title', 'message',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Blog_category)
class Blog_categoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)