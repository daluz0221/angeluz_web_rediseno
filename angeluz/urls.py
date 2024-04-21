"""
URL configuration for angeluz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', include(('aplications.home.urls', 'home'), namespace='home')),
    path('blog/', include(('aplications.blog.urls', 'blog'), namespace='blog')),
    path('faqs/', include(('aplications.faq.urls', 'faq'), namespace='faq')),
    path('servicios/', include(('aplications.service.urls', 'service'), namespace='service')),
    path('contacto/', include(('aplications.contact.urls', 'contact'), namespace='contact')),
    path('newsletter/', include(('aplications.newsletter.urls', 'newsletter'), namespace='newsletter')),
    path('users/', include(('aplications.users.urls', 'users'), namespace='users')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 



urlpatterns += [
    path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]