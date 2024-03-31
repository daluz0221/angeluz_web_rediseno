from django.db import models

# Create your models here.

from .managers import ServiceManager

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo', blank=True, null=True)
    summary = models.TextField(verbose_name='Resumen', blank=True, null=True)
    description = models.TextField(verbose_name='Descripción')
    icon = models.CharField(max_length=200, verbose_name='Icono',blank=True, null=True , help_text='Usar una clase de Fontawesome, consultar los iconos en https://fontawesome.com/search?m=free&o=r, icon que se verá en la home')
    image = models.ImageField(verbose_name='Imagen', upload_to='services', blank=True, null=True)
    active = models.BooleanField(verbose_name='Activo', default=True)
    destacado = models.BooleanField(verbose_name='Destacado', default=False)
    showHome = models.BooleanField(verbose_name='Mostrar en Home', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    objects = ServiceManager()

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title