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
    

class InfoSectionManager(models.Manager):
    """Manager para el modelo InfoSection"""

    def activos(self):
        return self.filter(
            active=True,
        ).order_by('orden')
    

class HeaderLinksManager(models.Manager):
    """Manager para el modelo HeaderLinks"""

    def get_menu_links(self):
        return self.filter(
            active=True,
        ).order_by('orden')
    
class InfoHomeManager(models.Manager):
    """Manager para el modelo InfoHome"""

    def activo(self):
        return self.filter(
            active=True,
        ).first()
    
    def get_whatsapp(self):
        try:
            return self.filter(
                active=True,
            ).first().whatsapp
        except:
            return 'No hay número de whatsapp registrado'