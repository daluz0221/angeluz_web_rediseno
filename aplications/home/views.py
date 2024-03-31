from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from aplications.service.models import Service
from aplications.blog.models import Entrada
from aplications.faq.models import Faq
from aplications.contact.forms import ContactForm

from .models import Background, InfoSection


class HomePageView(TemplateView):
    template_name = "home/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['servicios'] = Service.objects.home_services()
        context['entradas_home'] = Entrada.objects.filter(active=True, showHome=True)[:4]
        context['faqs_home'] = Faq.objects.home_faqs()
        context['background'] = Background.objects.background_page("1")
        context['contact_form'] = ContactForm
        context['infoSections'] = InfoSection.objects.activos()

        return context