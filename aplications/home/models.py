from django.db import models

# Create your models here.

from .managers import BackgroundManager, InfoSectionManager, HeaderLinksManager, InfoHomeManager

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

    objects = HeaderLinksManager()

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
    whatsapp = models.IntegerField(max_length=200, verbose_name='whatsapp', blank=True, null=True)
    email = models.EmailField(verbose_name='Correo electrónico', blank=True, null=True)
    mainUrl = models.URLField(verbose_name='URL principal', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    objects = InfoHomeManager()

    class Meta:
        verbose_name = 'información general'
        verbose_name_plural = 'información general'
        ordering = ['-created']

    def __str__(self):
        return 'Información de la página de inicio #{}'.format(self.id)
    

class InfoSection(models.Model):

    SECTION_CHOICES = [
        ('1', 'sobre mi'),
        ('2', 'faq'),
        ('3', 'entradas'),
        ('4', 'servicios'),
        ('5', 'newsletter'),
        ('6', 'contacto'),
    ]

    section = models.CharField(max_length=1, choices=SECTION_CHOICES, verbose_name='Sección')
    title = models.CharField(max_length=200, verbose_name='Título', blank=True, null=True)
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo', blank=True, null=True)
    content = models.TextField(verbose_name='Contenido', blank=True, null=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='home', blank=True, null=True)
    orden = models.SmallIntegerField(verbose_name='Orden', default=0)
    active = models.BooleanField(verbose_name='Activo', default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    objects = InfoSectionManager()

    class Meta:
        verbose_name = 'información de sección'
        verbose_name_plural = 'información de secciones'
        ordering = ['-created']

    def __str__(self):
        return 'Información de la sección {}'.format(self.section)
    


class Pagina(models.Model):

    SECTION_CHOICES = [
        ('1', 'servicios'),
        ('2', 'sobre nosotros'),
        ('3', 'preguntas frecuentes'),
        ('4', 'blog'),
        ('5', 'contacto'),
    ]

    codigo = models.CharField(max_length=1, verbose_name='Código', choices=SECTION_CHOICES)
    encabezado = models.CharField(max_length=200, verbose_name='Encabezado', blank=True, null=True)
    description = models.TextField(verbose_name='Descripción', blank=True, null=True)
    active = models.BooleanField(verbose_name='Activo', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['-created']

    def __str__(self):
        return self.codigo