from django import forms
from .models import *

class ingresar_hora(forms.ModelForm):
    class Meta:
        model = hora
        fields = '__all__'
