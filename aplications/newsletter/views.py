from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse_lazy
<<<<<<< HEAD

=======
from django.core.mail import send_mail
from django.template.loader import render_to_string
>>>>>>> 2ab4e91 (Terminada v1 del proyecto contaluz)
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
        
        template = 'newsletter_email_user_template.html'
        context = {
            'token': token,
        }
            
        subject = 'Confirmación de suscripción'
        message_to_send = render_to_string(template, context)
        

        try:
            send_mail(
            subject,
            '',
            None,
            [new_email.email],
            fail_silently=False,
            html_message=message_to_send
        )
        except Exception as e:
            print(e)
            return HttpResponse('Error al enviar el correo')
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