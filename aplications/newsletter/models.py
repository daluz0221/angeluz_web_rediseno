from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(verbose_name='Correo electrónico', unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    active = models.BooleanField(verbose_name='Activo', default=False)
    pendiente_alta = models.BooleanField(verbose_name='Pendiente de alta', default=True)
    email_baja = models.BooleanField(verbose_name='Pendiente de baja', default=False)
    token = models.CharField(max_length=10, verbose_name='Token', blank=True, null=True)

   

    class Meta:
        verbose_name = 'suscriptor'
        verbose_name_plural = 'suscriptores'
        ordering = ['-created']

    def __str__(self):
        return self.email