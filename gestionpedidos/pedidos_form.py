from django import forms
from .models import Pedido, Acta
from datetime import date

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = [
            'numero',
            'actividad',
            'acta',
            'fecha_ejecucion',
        ]
        labels = {
            'actividad': 'Actividad',  # Cambiar la etiqueta de 'id_actividad'
            'acta': 'Acta',  # Cambiar la etiqueta de 'id_acta'
            'fecha_ejecucion': 'Fecha de ejecución',
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'actividad': forms.Select(attrs={'class': 'form-control'}),
            'acta': forms.Select(attrs={'class': 'form-control'}),
            'fecha_ejecucion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'value': date.today().strftime('%Y-%m-%d')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filtrar las ACTAS con estado "Activa" para el campo id_acta
        self.fields['acta'].queryset = Acta.objects.filter(estado='1')
