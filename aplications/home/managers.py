from django.db import models




class BackgroundManager(models.Manager):
    """Manager para el modelo Background"""

    def activo(self):
        return self.filter(
            active=True,
        ).first()
    
    def activos(self):
        return self.filter(
            active=True,
        ).order_by('-created')
    
    def background_page(self, page):
        return self.filter(
            active=True,
            pagina=page,
        ).first()