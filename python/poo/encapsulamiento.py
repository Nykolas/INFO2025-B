class Persona:
	def __init__(self, nombre_alta, apellido_alta, edad_alta, promedio_alta = 0):
		self.__nombre = nombre_alta
		self.__apellido = apellido_alta
		self.__edad = edad_alta

	def getNombre(self):
		return self.__nombre.capitalize()

	def getApellido(self):
		return self.__apellido 
	def getEdad(self):
		return self.__edad

	def setEdad(self,nueva_edad):
		self.__edad = nueva_edad

#---------AFUERA-----------
lista_personas = list()

while True:
	n = input("ingrese nombre: ")
	a = input("ingrese apellido: ")
	e = input("ingrese edad: ")
	x = Persona(n,a,e)
	lista_personas.append(x)
	seguir = input("quiere seguir si o no: ")
	if seguir != 'si':
		break

for p in lista_personas:
	p.setEdad(100)
	print(f"{p.getNombre()}, tiene {p.getEdad()}")