from django.shortcuts import render
from .models import Producto


def Listar_Productos(request):

	#ORM
	#es qeuivalente a hacer un "select * from producto"
	#ESTO ES LA ORM Producto.objects.all()
	todos_productos = Producto.objects.all()
	#como resultado la variable todos_productos es una lista con objetos
	#de la clase productos (copiados de la BD)

	#para pasar los datos al template se usa un diccionario
	context = {}
	context['productos'] = todos_productos
	return render(request,'productos/listar.html', context)
	#el tempalte cuando recibe ese diccionario "contexto"
	#automaticamente lo desempaqueta, es decir en el template
	#tengo directamente una variable que se llama en este caso productos
	#EJ
	# al template le paso algo asi  {'prodcutos': [obj_coca,obj_leche,obj_pan]}
	# el template lo automaticamente en esto
	# productos = [obj_coca,obj_leche,obj_pan]
