'''
#Vamos a ver en este archivo:
#A) como se define una funcion
#B) como se le pasa parametros.
#C) una funcion puede o no retornar un valor.
#D) especializar los parametros:
#	-multiples parametros
#	-parametros por defecto
#	-parametros desconocidos

#A)
#Asi se define una funcion
#def nombre_funcion (parametros):
#	ACCIONES QUE ESTAN DENTRO DE LA FUNCION
def saludar():
	print(f"Te voy a saluar")
	print(f"Te estoy saludando")
	print(f"Ya te salude")

#Una vez que se definio la funcion, la llamo cada ves que la necesito
saludar()

#B)
#Definamos ahora una funcion con parametros.

def saludar(a_quien):
	#nombre solo tiene definicion aca ADENTRO.
	print(f"Hola {a_quien} como estas")

#lo que hace python es "por detras" como una asignacion
#siendo a_quien el parametro definido en la funcion
#y x la variable que se pasa como parametro
#a_quien = x
x = input("ingresa tu nombre: ")
saludar(x)
y = input("ingresa otro nombre: ")
saludar(y)


#C)
#Una funcion puede no devolver nada
#se define y se usa de la siguiente manera
def suma(a,b):
	r = a + b
	print(f"el resultado es {r}")

x = int(input("ingrese el primer numero: "))
y = int(input("ingrese el Segundo numero: "))
suma(x,y)
#ojo que r solo existe dentro de la funcion, porque esta definida dentro.
#print(r)
#cuando termina esto, yo mostre el resultado de la suma, pero no lo guarde

#Una funcion si puede devolver un valor
def suma(a,b):
	r = a + b
	return r

x = int(input("ingrese el primer numero: "))
y = int(input("ingrese el Segundo numero: "))
resultado = suma(x,y)
print(f"la suma da {resultado}")
'''
#D) -multiparametros
#si existen varios parametros, python tiene en cuenta el orden

#-parametros por defecto
'''
def calcular_precio(costo, iva = 1.21):
	total = costo * iva
	return total

#esto significa que yo puedo llamar a la funcion, con 2 parametors o 1 solo
o1 = calcular_precio(100)
o2 = calcular_precio(100,1.105)
print(o1)
print(o2)
'''
#-valores desconocidos

# *ARGS
#definir una funcion para recibir una cantidad dinamica de paremtros

#python va a guardar todos los paramteros que no tienen lugar en la definicion
#en una LISTA que se llama args

def saludar(nombre1,nombre2, *args):
	print(f"Hola {nombre1}")
	print(f"Hola {nombre2}")
	for i in args:
		print(f"Hola {i}")

saludar('Nicolas','Marianela','Carlos','Juan','Pedro')

def suma(*args):
	r=0
	for x in args:
		r += x
	return r

res1 = suma(3,4,5)
res2 = suma(2,14,15,67,87,98)
print(res1)
print(res2)

# **KWARGS
#lo mismo que antes, pero en lugar de guardar muchos valores 'desconocidos'
#en una lista, guarda pares clave valor en un diccionario


