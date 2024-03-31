from django.contrib import admin

# Register your models here.
from .models import Entrada, CategoriaEntrada, Tag, Comentario


class EntradaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('autor', "title", "active", "showHome", "destacado")
    ordering = ('autor', 'created')
    search_fields = ('title', 'created', 'autor__username', 'autor__email')
    date_hierarchy = 'created'
    list_filter = ('title', 'created', 'active', 'showHome', 'destacado')
    prepopulated_fields = {"slug": ("title",)}

class CategoriaEntradaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', "active")
    ordering = ('name', 'created')
    search_fields = ('name', 'created')
    date_hierarchy = 'created'
    list_filter = ('name', 'created', 'active')
    prepopulated_fields = {"slug": ("name",)}


class TagAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', "active")
    ordering = ('name', 'created')
    search_fields = ('name', 'created')
    date_hierarchy = 'created'
    list_filter = ('name', 'created', 'active')
    prepopulated_fields = {"slug": ("name",)}


class ComentarioAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('entrada', "autor", "active")
    ordering = ('entrada', 'created')
    search_fields = ('entrada', 'created', 'autor__username', 'autor__email')
    date_hierarchy = 'created'
    list_filter = ('entrada', 'created', 'active')


admin.site.register(Entrada, EntradaAdmin)
admin.site.register(CategoriaEntrada, CategoriaEntradaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comentario, ComentarioAdmin)