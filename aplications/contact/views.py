from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import CreateView, TemplateView

from aplications.home.models import Background

from .forms import ContactForm

class AddContactMessageView(CreateView):
    form_class = ContactForm
    success_url = reverse_lazy('contact_app:success')
    template_name = 'contacto/contact.html'

    def get_context_data(self, **kwargs):
        context = super(AddContactMessageView, self).get_context_data(**kwargs)
        context['background'] = context['background'] = Background.objects.background_page("5")
        context['info'] = {
            "title": "Contáctanos"
        }
        
        return context


class SuccessView(TemplateView):
    template_name = 'contacto/success.html'
    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['background'] = context['background'] = Background.objects.background_page("5")

        return context