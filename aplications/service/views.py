from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from aplications.home.models import Background, Pagina

from .models import Service


class ServicesListView(ListView):
    template_name = "services/list.html"
    queryset = Service.objects.activos()
    context_object_name = "services"
    

    def get_context_data(self, **kwargs):
        context = super(ServicesListView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page('4')
        context['info'] = Pagina.objects.filter(codigo='1')
        context['design1'] = 'sections/services/fragments/design_v1.html'
        context['design2'] = 'sections/services/fragments/design_v2.html'
        return context
    
class ServiceDetailView(DetailView):
    template_name = "services/detalle_v1.html"
    model = Service
    context_object_name = "servicio"

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page('4')
        return context
    