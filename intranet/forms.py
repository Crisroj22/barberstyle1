from django import forms
from intranet.models import Producto

class FormCliente(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'rut' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'nombre' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'genero' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'numero_telefonico' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            )
        }



class FormBodega(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'faltante' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'vendido' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'descuento' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'valor_unitario' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            )
        }
        

class FormBarbero(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'