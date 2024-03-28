from django import forms
from django.contrib.auth import authenticate
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir Contraseña',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = (
            'email',
            'name',
            'last_name',
            'cedula',
            'phone',
            'genero',
        )

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Correo Electronico',
                    'class': 'form-control'
                }
            ),
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombres',
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Apellidos',
                    'class': 'form-control'
                }
            ),
            'cedula': forms.TextInput(
                attrs={
                    'placeholder': 'cédula',
                    'class': 'form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': 'Telefono',
                    'class': 'form-control'
                }
            ),
            'genero': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            )
        }
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las contraseñas no son iguales')


class LoginForm(forms.Form):
    email = forms.CharField(
        label='E-mail',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Correo Electronico',
                'type': 'email',
                'class': 'form-control',
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'contraseña',
                'class': 'form-control',
                'type': 'password',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Actual'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña Nueva'
            }
        )
    )