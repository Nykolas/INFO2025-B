def contar_digitos_str(num):
	num_str = str(num)
	cant_dig = len(num_str)
	return cant_dig

def contar_digitos_div(numero):
	contador = 0
	while numero > 0:
		numero = numero // 10
		contador = contador + 1
	return contador

num_usuario = int(input("Ingresá un número: "))
resultado1 = contar_digitos_str(num_usuario)
resultado2 = contar_digitos_div(num_usuario)

print(f"USANDO LA FUNCION DE STR, El numero tiene {resultado1} dígitos.")
print(f"USANDO LA FUNCION DE DIV,, El numero tiene {resultado2} dígitos.")
