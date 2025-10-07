'''
def suma_listas(lista_entrada):
	suma = 0
	for n in lista_entrada:
		suma = suma + n
	return suma

lista0 = [36, 25, 64, 19, 7, 26, 46, 21, 87, 6, 71, 94, 71, 43, 34, 76, 60, 99, 41, 32, 17, 39, 17, 89, 1, 42, 61, 72, 43, 20]
lista1 = [8,6,11,23,118,21,145]
lista2 = [3,16,4,233,19]

s0 = suma_listas(lista0)
s1 = suma_listas(lista1)
s2 = suma_listas(lista2)
print(s0)
print(s1)
print(s2)
'''
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

