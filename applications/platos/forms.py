from django import forms
from .models import Platos

class CreacionPlatosForm(forms.ModelForm):
    class Meta:
        model=Platos
        fields=('__all__')
            
            
    def clean(self):
        nombre_plato=self.cleaned_data["Nombre_plato"]
        precio_plato= self.cleaned_data['precio_plato']
        if len(nombre_plato)==0:
            self.add_error('Nombre_plato','El nombre del plato no puede estar vacio')
        if precio_plato <= 0:
            self.add_error('precio_plato','el plato no puede ser negativo')
        
class ActualizarPlatosForm(forms.ModelForm):
    class Meta:
        model = Platos
        fields = ("__all__")
        