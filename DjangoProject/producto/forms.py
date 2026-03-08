from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'iva', 'stock', 'departamento']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del producto'}),
            'iva': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'IVA (%)'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad en stock'}),
            'departamento': forms.Select(attrs={'class': 'form-control'})
        }