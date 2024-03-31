from django.db import models


class ServiceManager(models.Manager):
    """Manager para el modelo Service"""

    def activos(self):
        return self.filter(
            active=True,
        ).order_by('created')

    def home_services(self):
        return self.filter(
            active=True,
            showHome=True,
        ).order_by('created')
    
    def hot_services(self):
        return self.filter(
            active=True,
            destacado=True,
        ).order_by('created')