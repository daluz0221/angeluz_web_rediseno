from django.contrib import admin

# Register your models here.
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', "description", "showHome", "destacado", "active")
    ordering = ('title', 'created')
    search_fields = ('title', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'active', 'showHome', 'destacado')


admin.site.register(Service, ServiceAdmin)