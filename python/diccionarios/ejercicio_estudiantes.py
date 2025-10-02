estudiantes = {}
cantidad = int(input("¿Cuántos estudiantes?: "))

# Ingresar los datos de cada estudiante
for i in range(cantidad):
	nombre = input("\nNombre: ")
	nota1 = float(input("Nota etapa 1: "))
	nota2 = float(input("Nota etapa 2: "))

	# Guardar notas y promedio en un diccionario dentro del diccionario principal
	estudiantes[nombre] = {
							"nota1": nota1,
							"nota2": nota2,
							"promedio": (nota1 + nota2) / 2
							}
# Buscar el estudiante con mejor promedio
mejor_estudiante = None
mejor_promedio = -1

print("\n===== Promedios de cada estudiante =====")
for nombre, datos in estudiantes.items():
	print(nombre, ":", datos["promedio"])
	if datos["promedio"] > mejor_promedio:
		mejor_promedio = datos["promedio"]
		mejor_estudiante = nombre

print("\nEl mejor promedio es de", mejor_estudiante, "con", mejor_promedio)

# LA SALIDA GENERADA POR GASTON ES  DE ESTA FORMA:

#{ 'Nicolas': {'nota1': 8.0, 'nota2': 8.0, 'promedio': 8.0}, 
#  'Marianela': {'nota1': 10.0, 'nota2': 9.0, 'promedio': 9.5} }

#SI QUEIRO SABER EL PROMEDIO DE NICOLAS

#LA FORMA DE ARIEL
#[ {'nombre':Nicolas,'nota1':8,'nota2':8, 'promedio':8},
#  {'nombre':Marianela,'nota1':9,'nota2':10, 'promedio':9.5} ]

#OTRA IDEA
#{ 'Nicolas': [8,8,8], 
#  'Marianela': [9,10,9.5] }
