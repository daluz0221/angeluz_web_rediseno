from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import FormView

from .utils import generate_token
from .models import Newsletter
from .forms import NewsletterSubscriptionForm, VerificationNewsletterForm


class NewsletterAddEmailView(FormView):
    form_class = NewsletterSubscriptionForm
    success_url = '/'
    template_name = 'newsletter/email_exist.html'

    def form_valid(self, form):
        token = generate_token()
        new_email = Newsletter(
                email=form.cleaned_data['email'],
                token=token
            )
        
        #Enviar email al usuario para que acepte si quiere que le lleguen cosas
        subject = 'Confirmación de suscripción'
        message = 'Para confirmar la suscripción da click en el siguiente enlace: ' +  ' ingresando el siguiente codigo' + token
        email_remitente = 'daluz0221@gmail.com'

        # send_mail(
        #     subject,
        #     message,
        #     email_remitente,
        #     [new_email.email],
        #     fail_silently=False,
        # )
        print(token)
        new_email.save()
        return HttpResponseRedirect(
            reverse_lazy('news_app:verification')
        )
    

    
class TokenNewsletterVerificationView(FormView):
    form_class = VerificationNewsletterForm
    template_name = 'newsletter/verification_newsletter.html'
    success_url = reverse_lazy('home_app:index')

    def form_valid(self, form):
        token = form.cleaned_data['token']
        if Newsletter.objects.filter(token=token).exists():
            newsletter = Newsletter.objects.get(token=token)
            newsletter.subscribed = True
            newsletter.save()
            return super(TokenNewsletterVerificationView, self).form_valid(form)
        else:
            raise Http404('Token no válido')
        
    def get_success_url(self):

        return reverse_lazy('home_app:index', kwargs={'message': 'ok'})