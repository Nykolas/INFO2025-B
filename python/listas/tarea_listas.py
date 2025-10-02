#guardar el nombre y las notas de la etapa 1 y 2
#de cada estudiante del informatorio
#y luego, mostrar quien es el estudiante con mejor promedio de nota

#estudiantes = [ ["nicolas",8,7], ['Marianlea',6,10],...[] ]

estudiantes = []

cantidad = int(input("¿Cuántos estudiantes?: "))

for i in range(cantidad):
	nombre = input("\nNombre: ")
	nota1 = float(input("Nota etapa 1: "))
	nota2 = float(input("Nota etapa 2: "))
	estudiantes.append([nombre, nota1, nota2])

# Calcular promedios y buscar el mejor
mejor_estudiante = ""
mejor_promedio = -1

print("\n===== Promedios de cada estudiante =====")
for est in estudiantes:
	nombre = est[0]
	n1 = est[1]
	n2 = est[2]
	promedio = (n1 + n2) / 2
	if promedio > mejor_promedio:
		mejor_promedio = promedio
		mejor_estudiante = nombre

print("\nEl mejor promedio es de", mejor_estudiante, "con", mejor_promedio)

#SOLUCION 2
estudiantes = []

while True:
	nombre = input("\nIngrese el nombre del estudiante (o 'salir' para terminar): ")

	if nombre.lower() == "salir":
		break

	nota1 = float(input("Ingrese la nota de la Etapa 1: "))
	nota2 = float(input("Ingrese la nota de la Etapa 2: "))
	promedio = (nota1 + nota2) / 2
	estudiantes.append([nombre, nota1, nota2, promedio])

mejor = estudiantes[0]
for est in estudiantes:
	if est[3] > mejor[3]:
		#est ya de por si es una lista
		mejor = est
#mejor es la lista que contiene la informacion del estudiante
# Acá mostramos el Resultado
print("\nEl estudiante con el mejor promedio es:")
print(f"Nombre: {mejor[0]}")
print(f"Etapa 1: {mejor[1]}")
print(f"Etapa 2: {mejor[2]}")
print(f"Promedio: {mejor[3]}")
