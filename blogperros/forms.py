from django import forms
from blogperros.models import Perro, Persona, Asignacion
from django.contrib.auth.models import User
from django.forms import ModelForm

class PerroForm(forms.ModelForm):
    class Meta:
        model = Perro
        fields = ('nombre', 'color','raza','fecha_nacimiento','imagen',)


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dpi', 'nombre','apellido','foto','perros',)
    def __init__ (self, *args, **kwargs):
        super(PersonaForm, self).__init__(*args, **kwargs)
        self.fields["perros"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["perros"].help_text = "Ingrese los Perros"
        self.fields["perros"].queryset = Perro.objects.all()


class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }
