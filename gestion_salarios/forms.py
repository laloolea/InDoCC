from django import forms
from gestion_salarios.models import Salarios


class SalariosForm(forms.ModelForm):

    class Meta:
        model = Salarios
        exclude = ['Salarios_id']
