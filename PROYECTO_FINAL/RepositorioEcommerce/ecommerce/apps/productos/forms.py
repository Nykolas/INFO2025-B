from django import forms
from .models import Producto

class FormularioCrearProducto(forms.ModelForm):
	#configurar cada atributo si lo deseo
	#por ejemplo que clase css tiene cada atributo
	class Meta:
		model = Producto
		fields = ['nombre','precio','stock','descripcion','imagen','rubro']

class FormularioModificarProducto(forms.ModelForm):

	class Meta:
		model = Producto
		fields = ['nombre','stock','descripcion','imagen']