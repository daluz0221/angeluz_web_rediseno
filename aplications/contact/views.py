from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
from django.views.generic import CreateView, TemplateView
from django.conf import settings

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
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        
        template = 'contact_email_template.html'
        context = {
            'nombre': name,
            'correo': email,
            'mensaje': message
        }
            
        subject = 'Nuevo mensaje de contacto'
        message_to_send = render_to_string(template, context)
        try:
            send_mail(
                subject,
                '',
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
                html_message=message_to_send
            )
        except Exception as e:
            print(e)
            return self.form_invalid(form)
        return super(AddContactMessageView, self).form_valid(form)


class SuccessView(TemplateView):
    template_name = 'contacto/success.html'
    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['background'] = context['background'] = Background.objects.background_page("5")

        return context