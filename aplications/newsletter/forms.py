from django import forms

from .models import Newsletter


class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        email_exists = Newsletter.objects.filter(email=email)
        if email_exists.exists():
            raise forms.ValidationError('El email ya se encuentra registrado')
        return email
    


class VerificationNewsletterForm(forms.Form):
    token = forms.CharField(max_length=10, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el token de verificación'}))
   
    # rest of the code...

    def clean_token(self):
        token = self.cleaned_data['token']
        email = Newsletter.objects.filter(token=token)
        if len(token) == 10:
            if not email.exists():
                raise forms.ValidationError('El token no es válido')
            email = email.first()
            email.active = True
            email.pendiente_alta = False
            email.save()
            return token
        else:
            raise forms.ValidationError('El token no es válido')