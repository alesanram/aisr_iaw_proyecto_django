from django import forms
from .models import Venta
from datetime import date, datetime


class VentaForm(forms.ModelForm):

    class Meta:
        model = Venta
        fields = ['codigo', 'cliente', 'producto', 'precio', 'cantidad', 'fecha']

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={
                'class': 'form-control',
                'id': 'id_producto'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'id_precio'
            }),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:
            self.fields['fecha'].initial = date.today()
            now = datetime.now()
            unix_last5 = str(int(now.timestamp()))[-5:]
            month_abbr = now.strftime("%b").upper()
            self.fields['codigo'].initial = f"{month_abbr}{unix_last5}"

