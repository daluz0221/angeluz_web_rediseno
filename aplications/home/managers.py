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
        
    def get_main_url(self):
        try:
            return self.filter(
                active=True,
            ).first().mainUrl
        except:
            return 'No hay URL principal registrada'
        
    def get_whatsapp_text(self):
        try:
            text = self.filter(
                active=True,
            ).first().textoWhatsapp
            text = text.replace(' ', '%20').replace('\n', '%0A').replace(',', '%2C').replace('.', '%2E').replace(';', '%3B').replace(':', '%3A').replace('?', '%3F').replace('¿', '%C2%BF').replace('¡', '%C2%A1').replace('!', '%21').replace('á', '%C3%A1').replace('é', '%C3%A9').replace('í', '%C3%AD').replace('ó', '%C3%B3').replace('ú', '%C3%BA').replace('Á', '%C3%81').replace('É', '%C3%89').replace('Í', '%C3%8D').replace('Ó', '%C3%93').replace('Ú', '%C3%9A').replace('ñ', '%C3%B1').replace('Ñ', '%C3%91')
            return text
        except:
            return 'No hay texto de whatsapp registrado'