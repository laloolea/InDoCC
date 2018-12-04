from django import forms
from gestion_promocion.models import Promocion


class PromocionForm(forms.ModelForm):

    class Meta:
        model = Promocion
        exclude = ['Promocion_id']