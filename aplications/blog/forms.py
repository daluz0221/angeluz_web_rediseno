from django import forms


from .models import Comentario


class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = (
            'comment',
        )

        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control', 'rows':4, 'placeholder':'Escribe tu comentario...'}),
        }