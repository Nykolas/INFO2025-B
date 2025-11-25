from django.shortcuts import render

def Listar_Productos(request):

	return render(request,'productos/listar.html')
