from django.urls import path
from . import views

app_name = 'contact_app'

urlpatterns = [
    path('', views.AddContactMessageView.as_view(), name='contact'),
    path('success/', views.SuccessView.as_view(), name='success'),
    # Agrega aquí más rutas de URL según tus necesidades
]
