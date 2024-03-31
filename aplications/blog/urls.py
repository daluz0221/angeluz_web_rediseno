from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    path(
        '', 
        views.EntradaListView.as_view(),
        name='entradas'
    ),
]