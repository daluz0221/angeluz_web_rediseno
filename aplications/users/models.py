from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField('Nombres', max_length=100)
    last_name = models.CharField('Apellidos', max_length=100)
    cedula = models.CharField('Cedula', max_length=20)
    phone = models.CharField('Telefono', max_length=20)
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    #
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['name']

    objects = UserManager()
    
    def get_full_name(self):
        return self.name + ' ' + self.last_name
    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.get_full_name() + ' - ' + self.email