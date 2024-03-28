from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, FormView
# Create your views here.


class FaqView(ListView):
    template_name = "faq/faqs.html"
    queryset = ['1', '2', '3', '4', '5']