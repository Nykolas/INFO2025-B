#diccionario se definen con {}
#nombre = {'clave':valor}
#las claves GENERALEMNTE, son o elementos simples (numeros o palabras)
#las claves NO SE PUEDEN REPETIR
#los valores pueden ser "cualquier cosa"
#osea, el valor puede ser: un numero, una palabra, una lista o un diccionario

#como se crea un diccionario vacio
#estudiantes = {}
#estudiantes = dict()

#como creo un diccionario con valores previos
#ejemplo de diccionario de edades
estudiantes = {'Nicolas':36, 'Marianela':20,'Kevin':21}
#como lo recorro?
'''
#por defecto si lo recorro asi, est vale la clave de cada posicion
for est in estudiantes:
	print(est)
#para recorrer clave y valor al mismo tiempo, se usa la funcion items()
for k,v in estudiantes.items():
	print(f"{k}----{v}")
#si quiero recorre solo el valor existe la funcion values()
for est in estudiantes.values():
	print(est)
'''
#COMO CARGO UN DICCIONARIO
#Creo una clave elio y le pongo el valor de 25
estudiantes['Elio'] = 25
#PERO SI ESA CLAVE YA EXISTE, MODIFICA SU VALOR
estudiantes['Nicolas'] = 80
#Como saber si una clave existe
nombre = input("ingrese un nombre: ")
if nombre in estudiantes.keys():
	print("EXISTE")
else:
	print("NO EXISTE")
print(estudiantes)