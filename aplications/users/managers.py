from django.db import models
from django.core.mail import send_mass_mail
#
from django.contrib.auth.models import BaseUserManager
from django.conf import settings


class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, password, is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        # message1 = ('Bienvenido a Angeluz', 'Gracias por registrarte en nuestra plataforma', None, [email])
        # message2 = ('Nuevo usuario registrado', 'Se ha registrado un nuevo usuario', None, [settings.DEFAULT_FROM_EMAIL])
        # send_mass_mail(
        #     (message1, message2),
        #     fail_silently=False
        # )
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, True, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, True, True, **extra_fields)