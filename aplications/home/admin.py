from django.contrib import admin

# Register your models here.

from .models import Background, RedesSociales, HeaderLinks, InfoHome, InfoSection, Pagina


class BackgroundAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'pagina', 'url', 'active')
    ordering = ('pagina', 'created')
    search_fields = ('title', 'created', 'pagina')
    date_hierarchy = 'created'
    list_filter = ('created', 'pagina', 'active')


class RedesSocialesAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('icon', 'url', 'active')
    ordering = ('orden', 'created')
    search_fields = ('created', 'icon')
    date_hierarchy = 'created'
    list_filter = ('created','active')


class HeaderLinksAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'url', 'orden', 'active')
    ordering = ('orden', 'created')
    search_fields = ('created', 'name')
    date_hierarchy = 'created'
    list_filter = ('created', 'active')
    list_editable = ('orden', 'active')

class InfoHomeAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('webTitle', 'mainUrl', 'eslogan', 'phone', 'whatsapp', 'email', 'active')
    ordering = ('created', 'webTitle')
    search_fields = ('webTitle', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'active')

class InfoSectionAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('section', 'orden', 'active')
    ordering = ('created', 'title')
    search_fields = ('title', 'created')
    date_hierarchy = 'created'
    list_filter = ('created', 'section', 'active')
    list_editable = ('orden', 'active')

class PaginaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('codigo', 'active')
    ordering = ('created',)
    search_fields = ('created',)
    date_hierarchy = 'created'
    list_filter = ('codigo', 'active')
    list_editable = ('active',)


admin.site.register(Background, BackgroundAdmin)
admin.site.register(RedesSociales, RedesSocialesAdmin)
admin.site.register(HeaderLinks, HeaderLinksAdmin)
admin.site.register(InfoHome, InfoHomeAdmin)
admin.site.register(InfoSection, InfoSectionAdmin)
admin.site.register(Pagina, PaginaAdmin)




