from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    path(
        '', 
        views.EntradaListView.as_view(),
        name='entradas'
    ),
    path(
        'categoria/<slug>/', 
        views.CategoryEntradaListView.as_view(),
        name='categoria'
    ),
    path(
        'tag/<slug>/', 
        views.TagEntradaListView.as_view(),
        name='tag'
    ),
    path(
        'entrada/<slug>/', 
        views.EntradaDetalleView.as_view(),
        name='entrada'
    ),
]