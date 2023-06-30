from django import forms
from .models import mesa

class CreateMesasForms(forms.ModelForm):
    class Meta:
        model=mesa
        fields=("numero_mesa",)
        
    def clean(self):
        cleaned_data = super().clean()
        n_mesa = cleaned_data.get('numero_mesa')
        if n_mesa<=0 or n_mesa >30:
            self.add_error('numero_mesa', 'numero mesa no puede ser menor o igual que 0 y no puede ser mayor de 30')

        return cleaned_data