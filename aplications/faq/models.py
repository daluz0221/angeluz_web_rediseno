from django.db import models

# Create your models here.


from .managers import FaqsManager

class Faq(models.Model):
    question = models.CharField(max_length=200, verbose_name='Pregunta')
    answer = models.TextField(verbose_name='Respuesta')
    active = models.BooleanField(verbose_name='Activo', default=True)
    orden = models.PositiveIntegerField(verbose_name='Orden', default=0)
    showHome = models.BooleanField(verbose_name='Mostrar en Home', default=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    objects = FaqsManager()

    class Meta:
        verbose_name = 'pregunta frecuente'
        verbose_name_plural = 'preguntas frecuentes'
        ordering = ['-created']

    def __str__(self):
        return self.question
    

