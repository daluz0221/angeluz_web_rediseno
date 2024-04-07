from django.urls import path

from . import views

app_name = 'news_app'

urlpatterns = [
    path(
        'sucription',
        views.NewsletterAddEmailView.as_view(),
        name='sucription'
    ),
    path(
        'verification/',
        views.TokenNewsletterVerificationView.as_view(),
        name='verification'
    ),
]