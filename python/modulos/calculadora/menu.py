import os
OPCIONES = [
		(1, 'Sumar'),
		(2, 'Restar'),
		(3, 'Dividir'),
		(4, 'Multiplicar'),
		(5, 'Salir'),
]
def menu():
	os.system('cls')
	while True:
		for op in OPCIONES:
			print(f"{op[0]}: {op[1]}")
		respuesta = int(input())
		
		if respuesta > len(OPCIONES):
			print("INGRESE UNA OPCION VALIDA")
		else:
			break

	return respuesta