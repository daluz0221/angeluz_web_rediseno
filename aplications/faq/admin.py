from django.contrib import admin

# Register your models here.

from .models import Faq

class FaqAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('question', "answer", "showHome", "orden", "active")
    ordering = ('question', 'created')
    search_fields = ('question', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'active', 'showHome')
    list_editable = ('showHome', 'active', 'orden')

admin.site.register(Faq, FaqAdmin)