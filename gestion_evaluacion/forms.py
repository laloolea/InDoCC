from django import forms
from gestion_evaluacion.models import Evaluacion


class EvaluacionForm(forms.ModelForm):

    class Meta:
        model = Evaluacion
        exclude = ['Evaluacion_id']