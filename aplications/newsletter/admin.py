from django.contrib import admin

# Register your models here.

from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('email', 'active', 'pendiente_alta', 'email_baja')
    ordering = ('email', 'created')
    search_fields = ('email', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'active', 'pendiente_alta', 'email_baja')

admin.site.register(Newsletter, NewsletterAdmin)