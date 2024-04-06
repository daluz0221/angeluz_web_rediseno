from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView

from aplications.home.models import Background


from .forms import ComentarioForm
from .models import Entrada, CategoriaEntrada, Tag, Comentario

class EntradaListView(ListView):
    template_name = "blog/list.html"
    queryset = Entrada.objects.entradas_home()
    paginate_by = 6
    context_object_name = 'entradas'


    def get_context_data(self, **kwargs):
        context = super(EntradaListView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page(3)
        context['categorias'] = CategoriaEntrada.objects.categorias_activas()
        context['tags'] = Tag.objects.tags_activos()
        context['entradas_destcadas'] = Entrada.objects.entradas_destacadas()
        return context


class EntradaDetalleView(FormMixin, DetailView):
    template_name = "blog/detail.html"
    model = Entrada
    context_object_name = "entrada"
    form_class = ComentarioForm
    
    def get_success_url(self):
        return self.request.path

    def get_context_data(self, **kwargs):
        context = super(EntradaDetalleView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page('3')
        context['entradas'] = Entrada.objects.entradas_destacadas()	
        context['categorias'] = CategoriaEntrada.objects.categorias_activas()
        context['comentarios'] = Comentario.objects.comentarios_entrada(self.kwargs['slug'])
        context['form'] = self.get_form()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        

    def form_valid(self, form):
        form.instance.entrada = self.object
        form.instance.autor = self.request.user
        form.save()
        return super(EntradaDetalleView, self).form_valid(form)
    

class CategoryEntradaListView(ListView):
    template_name = "blog/list.html"
    paginate_by = 6
    context_object_name = "entradas"
    

    def get_queryset(self):
        return Entrada.objects.entradas_categoria(self.kwargs['slug'])
    

    def get_context_data(self, **kwargs):
        context = super(CategoryEntradaListView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page('3')
        context['categoria'] = CategoriaEntrada.objects.get(slug=self.kwargs['slug'])
        context['categorias'] = CategoriaEntrada.objects.categorias_activas()
        context['tags'] = Tag.objects.tags_activos()
        context['entradas_destcadas'] = Entrada.objects.entradas_destacadas()
        return context
    

class TagEntradaListView(ListView):
    template_name = "blog/list.html"
    paginate_by = 6
    context_object_name = "entradas"
    

    def get_queryset(self):
        return Entrada.objects.entradas_tag(self.kwargs['slug'])
    

    def get_context_data(self, **kwargs):
        context = super(TagEntradaListView, self).get_context_data(**kwargs)
        context['background'] = Background.objects.background_page('3')
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        context['categorias'] = CategoriaEntrada.objects.categorias_activas()
        context['tags'] = Tag.objects.tags_activos()
        context['entradas_destcadas'] = Entrada.objects.entradas_destacadas()
        return context
