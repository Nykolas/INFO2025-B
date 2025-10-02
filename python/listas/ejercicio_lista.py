lista = [36, 25, 64, 19, 7, 26, 46, 21, 87, 6, 71, 94, 71, 43, 34, 76, 60, 99, 41, 32, 17, 39, 17, 89, 1, 42, 61, 72, 43, 20]
suma = 0
mayor = 0
# suma
for n in lista:
	suma = suma + n
	if n > mayor:
		mayor = n

print("La suma de los numeros de la lista es ", suma)
# promedio
#len() retorna cuantos elementos tiene la lista
promedio = suma / len(lista)
print("El promedio de los números de la lista es ", promedio)
# numero mayor
print("El número mas grande de la lista es ", mayor)

print("----------------------------")

print("EL MAYOR ELEMENTO ES, ", max(lista))
print("LA SUMA DE LOS ELEMENTOS ES, ", sum(lista))
print("EL PROMEDIO ES, ", sum(lista)/len(lista))