'''
#las listas se definen y/o usan con corchetes []
lista_estudiantes = ['Nicolas', 'Marianela','Ariel','Kevin','Elio']

#las listas en python son heterogeneas
#ej ['Nicolas',35,[5,33]]
print(lista_estudiantes)
print(lista_estudiantes[1])

#ambas formas, crean una lista vacia.
#lista_estudiantes = list()

lista_estudiantes = []
print(lista_estudiantes)

#funciones o metodos de una lista
#los metodos se usan "generalemnte" como
#nombre_lista.metodo()
#para agregar un elemento se usa el metodo
#append
lista_estudiantes.append('Nicolas')
print(lista_estudiantes)

#ejercicio de cargar una lista de nombres
#Solucion 1
estudiantes = []
cantidad = int(input("¿Cuántos estudiantes quieres cargar? "))

#cantidad = 5, range hace [0,1,2,3,4]
for i in range(cantidad):
	nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
	estudiantes.append(nombre)

print("\nLista de estudiantes:")

#si estudiantes vale por ejemplo 
#['Nicolas', 'Marianela','Ariel','Kevin','Elio']
for est in estudiantes:
	print("-", est)


#Solucion 2
alumnos = []
continuar = "si"

while continuar == "si":
	alumno = input("Ingrese el nombre del alumno. ")
	alumnos.append(alumno)
	continuar = input("quiere continuar Si o No: ")

for est in alumnos:
	print("-", est)


#Ejemplo de otro metodo
#Recorrer una lista al reves
estudiantes = ['Nicolas', 'Marianela','Ariel','Kevin','Elio']

estudiantes.reverse()

for i in estudiantes:
	print("-", i)
'''
import random
lista = []

for x in range(30):
	lista.append(random.randint(1,100))

print(lista)