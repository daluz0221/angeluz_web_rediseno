from django.db import models

# Create your models here.

from .managers import BackgroundManager

class Background(models.Model):

    SECTION_CHOICES = [
        ('1', 'home'),
        ('2', 'faq'),
        ('3', 'entradas'),
        ('4', 'servicios'),
        ('5', 'contacto'),
    ]


    title = models.CharField(max_length=200, verbose_name='Título', blank=True, null=True)
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo', blank=True, null=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='home')
    pagina = models.CharField(max_length=1, choices=SECTION_CHOICES, verbose_name='Página', default='1')
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    button = models.CharField(max_length=200, verbose_name='Botón', blank=True, null=True)
    active = models.BooleanField(verbose_name='Activo', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    objects = BackgroundManager()

    class Meta:
        verbose_name = 'fondo'
        verbose_name_plural = 'fondos'
        ordering = ['-created']

    def __str__(self):
        if self.title:
            return self.title
        return 'Background de la página {}'.format(self.pagina)