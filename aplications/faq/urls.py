from django.urls import path

from . import views

app_name = 'faq_app'

urlpatterns = [
    path(
        '', 
        views.FaqView.as_view(),
        name='faq'
    ),
]