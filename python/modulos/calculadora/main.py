from operaciones import sumar,restar,multiplicar,dividir
from menu import menu
print("-------CALCULADORA-------")

opcion = menu()

while opcion != 5:
	
	x = int(input("INGRESE NUMERO 1: "))
	y = int(input("INGRESE NUMERO 2: "))

	if opcion == 1:
		r = sumar(x,y)
	elif opcion == 2:
		r = restar(x,y)
	elif opcion == 3:
		r = dividir(x,y)
	elif opcion == 4:
		r = multiplicar(x,y)

	print(f"el resultado de la operacion es: {r}")
	input("Presione enter para continuar...")
	opcion = menu()

print("GRACIAS POR USAR !CALCULADORA!")