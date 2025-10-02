
# EJERCICIO CON CONDICioNAL SIMPLE
# PROGRAMA QUE PERMITA COMPRAR LA CANTIDAD DESEADA DE UN SOLO PRODUCTO
# Y SI EL TOTAL ES MAYOR A 10000 EXISTE UN DESCUENTRO DEL 10%
'''
 = int(input("Ingrese el precio del producto: "))
cant = int(input("Ingrese la cantidad comprada: "))

total = precio * cant

if total > 10000:
	total = total - (total*10/100)
	print("Usted tiene un 10% de descuento")

print(f"Usted debe pagar un total de {total}")
'''
#EJERCICIO CON CONDICIONAL ALTERNATIVO
# PROGRAMA QUE PERMITA COMPRAR LA CANTIDAD DESEADA DE UN SOLO PRODUCTO
# Y SI EL TOTAL ES MAYOR A 10000 EXISTE UN DESCUENTRO DEL 10%,
# CASO CONTRARIO EL DESCUENTO ES SOLO DEL 5%
'''
precio = int(input("Ingrese el precio del producto: "))
cant = int(input("Ingrese la cantidad comprada: "))

total = precio * cant

if total > 10000:
	total = total - (total*10/100)
	print("Usted tiene un 10% de descuento")
else:
	total = total - (total*5/100)
	print("Usted tiene un 5% de descuento")

print(f"Usted debe pagar un total de {total}")
'''

# PROGRAMA QUE PERMITA COMPRAR LA CANTIDAD DESEADA DE UN SOLO PRODUCTO
# Y SI EL TOTAL ES MAYOR A 10000 EXISTE UN DESCUENTRO DEL 10%,
# CASO CONTRARIO EL DESCUENTO ES SOLO DEL 5%
# Ademas si la compra supera lo 10000, y la cantidad de productos es mayor a 3
# se agrega un descuento del 7%.
precio = int(input("Ingrese el precio del producto: "))
cant = int(input("Ingrese la cantidad comprada: "))

total = precio * cant

if total > 10000:
	total = total - (total*10/100)
	print("Usted tiene un 10% de descuento")
	if cant > 3:
		total = total - (total * 7/100)
		print("Ademas como su compra fue de mas de 3 prodcutos, se le suma un 7%")
else:
	total = total - (total*5/100)
	print("Usted tiene un 5% de descuento")

print(f"Usted debe pagar un total de {total}")