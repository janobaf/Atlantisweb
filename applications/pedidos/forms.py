from django import forms
from .models import PlatoPedidos,pedidos


class CreacionPlatosForm(forms.ModelForm):
    class Meta:
        model = PlatoPedidos
        fields=("__all__")
    def clean(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad<=0:
            self.add_error('cantidad','la cantidad no puede ser negativo')

class CreacionPedidosForm(forms.ModelForm):
    class Meta:
        model=pedidos
        fields=(
            'id',
            'mesa',
            )
    