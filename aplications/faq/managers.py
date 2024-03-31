from django.db import models



class FaqsManager(models.Manager):
    """Manager para el modelo Faq"""

    def home_faqs(self):
        return self.filter(
            active=True,
            showHome=True,
        ).order_by('orden')[:5]
    
    def activos(self):
        return self.filter(
            active=True,
        ).order_by('orden')