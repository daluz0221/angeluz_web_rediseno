from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, FormView
# Create your views here.

from aplications.home.models import Background, Pagina

from .models import Faq


class FaqView(ListView):
    template_name = "faq/faqs.html"
    queryset = Faq.objects.activos()

    def get_context_data(self, **kwargs):
        context = super(FaqView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page("2")
        context['faqs'] =Faq.objects.activos()
        context['section'] = Pagina.objects.get(codigo='3')
        return context