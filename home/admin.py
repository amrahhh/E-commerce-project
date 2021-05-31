from django.contrib import admin
from home.models import (
    Alliance,
)
# Register your models here.

@admin.register(Alliance)
class AllianceAdmin(admin.ModelAdmin):
    list_display = ('image',)
    list_filter = ('image',)
    search_fields = ('image',)