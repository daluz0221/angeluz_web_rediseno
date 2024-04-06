from django.db import models


class EntradaManager(models.Manager):
    """Manager para el modelo Entrada"""

    def entradas_activas(self):
        return self.filter(
            active=True,
        ).order_by('-created')
    
    def entradas_home(self):
        return self.filter(
            active=True,
            showHome=True,
        ).order_by('-created')
    
    def entradas_destacadas(self, limit=3):
        return self.filter(
            active=True,
            destacado=True,
        ).order_by('-created')[:limit]
    
    def entradas_categoria(self, categoria):
        return self.filter(
            active=True,
            categoria__slug=categoria,
        ).order_by('-created')
    
    def entradas_tag(self, tag):
        return self.filter(
            active=True,
            tags__slug=tag,
        ).order_by('-created')
    
    
    


class CategoriaEntradaManager(models.Manager):
    """Manager para el modelo CategoriaEntrada"""

    def categorias_activas(self):
        return self.filter(
            active=True,
        ).order_by('-created')
    
    
    

class TagManager(models.Manager):
    """Manager para el modelo Tag"""

    def tags_activos(self):
        return self.filter(
            active=True,
        ).order_by('-created')
    

class ComentarioManager(models.Manager):

    def comentarios_entrada(self, entrada):
        return self.filter(
            active=True,
            entrada__slug=entrada,
        ).order_by('-created')
    

class Comentario2Manager(models.Manager):

    def comentarios_entrada(self, comentario):
        return self.filter(
            active=True,
            comentario_padre=comentario,
        ).order_by('-created')