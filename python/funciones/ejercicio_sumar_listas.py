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
