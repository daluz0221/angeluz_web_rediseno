from django.db import models
from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField

from aplications.users.models import User
# Create your models here.



class CategoriaEntrada(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    slug = models.SlugField(max_length=100, verbose_name='Slug', unique=True)
    active = models.BooleanField(verbose_name='Activo', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # objects = CategoriaEntradaManager()

    class Meta:
        verbose_name = 'categoría de entrada'
        verbose_name_plural = 'categorías de entradas'
        ordering = ['-created']

    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    slug = models.SlugField(max_length=100, verbose_name='Slug')
    active = models.BooleanField(verbose_name='Activo', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # objects = TagManager()

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['-created']

    def __str__(self):
        return self.name

class Entrada(models.Model):
    categoria = models.ForeignKey(CategoriaEntrada, verbose_name='Categoría', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags')
    title = models.CharField(max_length=200, verbose_name='Título')
    slug = models.SlugField(max_length=200, verbose_name='Slug', unique=True)
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    description = RichTextUploadingField('Contenido')
    summary = models.TextField(verbose_name='Resumen', blank=True, null=True)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog')
    active = models.BooleanField(verbose_name='Activo', default=True)
    destacado = models.BooleanField(verbose_name='Destacado', default=False)
    showHome = models.BooleanField(verbose_name='Mostrar en Home', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # objects = EntradaManager()

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']

    def save(self, *args, **kawrgs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Entrada, self).save(*args, **kawrgs)

    def __str__(self):
        return self.title
    


class Comentario(models.Model):
    entrada = models.ForeignKey(Entrada, verbose_name='Entrada', on_delete=models.CASCADE)
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comentario')
    active = models.BooleanField(verbose_name='Activo', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')


    # objects = ComentarioManager()

    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
        ordering = ['-created']

    def __str__(self):
        return self.autor.name
