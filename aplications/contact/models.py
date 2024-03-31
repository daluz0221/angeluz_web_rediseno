from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo electrónico')
    message = models.TextField(verbose_name='Mensaje')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    pending = models.BooleanField(verbose_name='Pendiente', default=True)
    reviewed = models.BooleanField(verbose_name='Revisado', default=False)

    def reviewed_true(self):
        if self.pending == True:
            self.reviewed = False
        elif self.pending == False:
            self.reviewed = True
        self.save()

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering = ['-created']

    def __str__(self):
        return self.name