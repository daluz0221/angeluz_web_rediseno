from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView



class ServicesListView(ListView):
    template_name = "services/list.html"
    queryset = ['1', '2', '3', '4', '5']