class Persona:
	#atributos
	#este metodo se ejecuta siempre y, si o si cuando creo una persona
	#es el que crea
	def __init__(self, nombre_alta, apellido_alta, edad_alta, promedio_alta = 0):
		self.nombre = nombre_alta
		self.apellido = apellido_alta
		self.edad = edad_alta
		self.promedio = promedio_alta
	#metodos (funciones)
	#self recibe el objeto que pidio el metodo
	def getNombre(self):
		return self.nombre
	def getApellido(self):
		return self.apellido 
	def getEdad(self):
		return self.edad
	def getPromedio(self):
		return self.promedio

	def setPromedio(self, nuevo_promedio):
		self.promedio = nuevo_promedio

# crear una lista con personas
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
print("---------------------------------")		
print("Usted cargo a estas personas: ")
for p in lista_personas:
	print(f"el estudiante {p.getNombre()}, tiene un promedio de {p.getPromedio()}")

while True:
	nombre = input("ingrese el nombre del estudiante para cambiar su promedio ")
	for p in lista_personas:
		if p.getNombre() == nombre:
			promedio = float(input(f"ingrese el nuevo promedio del estudiante {nombre}"))
			p.setPromedio(promedio)
	seguir = input("quiere seguir si o no: ")
	if seguir != 'si':
		break
print("---------------------")
print("los nuevos promedio son")
for p in lista_personas:
	print(f"el estudiante {p.getNombre()}, tiene un promedio de {p.getPromedio()}")


