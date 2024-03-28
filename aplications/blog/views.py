from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView

from aplications.home.models import Background



class EntradaListView(ListView):
    template_name = "blog/list.html"
    queryset = ['1', '2', '3', '4', '5']
    