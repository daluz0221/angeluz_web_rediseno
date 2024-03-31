from django.contrib import admin

# Register your models here.
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pending', 'reviewed')
    search_fields = ('name', 'email', 'message')
    list_filter = ('pending', 'reviewed', 'created', 'pending')

admin.site.register(Contacto, ContactoAdmin)