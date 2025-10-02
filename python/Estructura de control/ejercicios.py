'''
numero = int(input("Ingrese un número: "))

#el operador % retorna el resto de la division
# 10 / 2 la division da 5 y el resto 0
# 7 / 2 la division da 3 y el resto 1
if numero % 2 == 0:
	print("El número es par.")
else:
	print("El número es impar.")
#hagamos lo mismo pero sin usar el operador %

numero = int(input("Ingrese un número: "))

while numero > 1:
	numero = numero - 2

if numero == 0:
	print("el numero ingresado es par")
else:
	print("el numero ingresado es impar")
'''

numero = 24
intento = 5

while intento > 0:
	x = int(input("Ingrese un numero: "))
	if x != numero:
		print ("El numero ingresado no coincide")
		intento = intento - 1
		print(f"te quedan {intento} intentos...")
	else:
		print ("El numero es correcto")
		# el break termina obligatoriamente el ciclo
		break

if intento == 0:
	print("perdio todos los intentos....")

