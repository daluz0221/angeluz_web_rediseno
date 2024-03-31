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
    
class RedesSociales(models.Model):

    ICON_CHOICES = [
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('instagram', 'instagram'),
        ('linkedin', 'linkedin'),
        ('youtube', 'youtube'),
        ('whatsapp', 'whatsapp'),
        ('telegram', 'telegram'),
        ('github', 'github'),
        ('gitlab', 'gitlab'),
        ('bitbucket', 'bitbucket'),
        ('tiktok', 'tiktok'),
    ]

    icon = models.CharField(max_length=20, choices=ICON_CHOICES, verbose_name='Icono')
    orden = models.SmallIntegerField(verbose_name='Orden', default=0)
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    active = models.BooleanField(verbose_name='Activo', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'red social'
        verbose_name_plural = 'redes sociales'
        ordering = ['-created']

    def __str__(self):
        return self.icon
    
class HeaderLinks(models.Model):

    name = models.CharField(max_length=200, verbose_name='Nombre')
    url = models.URLField(verbose_name='URL', blank=True, null=True)
    orden = models.SmallIntegerField(verbose_name='Orden', default=0)
    active = models.BooleanField(verbose_name='Activo', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'enlace del menú'
        verbose_name_plural = 'enlaces del menú'
        ordering = ['-orden']

    def __str__(self):
        return self.name
    

class InfoHome(models.Model):

    webTitle = models.CharField(max_length=200, verbose_name='Título de la web', help_text='texto que se mostrará en la pestaña del navegador')
    logoHome = models.ImageField(verbose_name='Logo de la web', upload_to='home', blank=True, null=True)
    eslogan = models.CharField(max_length=200, verbose_name='Eslogan', blank=True, null=True)
    active = models.BooleanField(verbose_name='Activo', default=False)
    phone = models.CharField(max_length=200, verbose_name='Teléfono', blank=True, null=True)
    email = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)
    mainUrl = models.URLField(verbose_name='URL principal', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'información de la página de inicio'
        verbose_name_plural = 'información de la página de inicio'
        ordering = ['-created']

    def __str__(self):
        return 'Información de la página de inicio #{}'.format(self.id)
    

class InfoSection(models.Model):

    SECTION_CHOICES = [
        ('1', 'home'),
        ('2', 'faq'),
        ('3', 'entradas'),
        ('4', 'servicios'),
        ('5', 'contacto'),
        ('6', 'sobre mi'),
    ]

    section = models.CharField(max_length=1, choices=SECTION_CHOICES, verbose_name='Sección')
    title = models.CharField(max_length=200, verbose_name='Título', blank=True, null=True)
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo', blank=True, null=True)
    content = models.TextField(verbose_name='Contenido', blank=True, null=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='home', blank=True, null=True)
    active = models.BooleanField(verbose_name='Activo', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'información de sección'
        verbose_name_plural = 'información de secciones'
        ordering = ['-created']

    def __str__(self):
        return 'Información de la sección {}'.format(self.section)