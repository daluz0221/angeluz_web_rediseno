from django.urls import path

from . import views

app_name = 'service_app'

urlpatterns = [
    path(
        '', 
        views.ServicesListView.as_view(),
        name='servicio'
    ),
]