nombre = "Nicolas"
edad = 36
domicilio = "25 de mayo 1000"
altura = 1.80
'''
#MOSTRAR MENSAJE POR PANTALLA
print("HOLA MUNDO")
#MOSTRAR EL CONTENIDO DE LA VARIABLE
print(nombre)
#MOSTRAR MENSAJE LITERAL MEZCLADO CON VARIABLEs
# f viene de format
print(f"Nombre {nombre}, edad {edad}")
# version sin f
print("Nombre ", nombre, ", edad ", edad)

#TIPOS DE DATOS EN PYTHOn
print(type(nombre)) # string = cadena = alfanumerico
print(type(edad))	# int = integer = entero
print(type(domicilio))
print(type(altura)) #float = numero decimal o numero real

#Capturar un valor ingresado por el usuario
x = input("ingresa tu nombre: ")
#input puede funcionar como un escribir y leer al mismo tiempo
y = input("ingrese un numero: ")
# EN PYTHON SIEMPRE QUE SE INGRESE UN VALOR POR PANTALLA,
# ESE VALOR ES UN STRING
print(f"la variable x vale = {x} y es del tipo {type(x)}")
print(f"la variable y vale = {y} y es del tipo {type(y)}") 
#PARSER
#SI NECESITO UN NUMERO, AL INPUT LO PASO A ENTERO CON LA FUNCION int
z = int(input("ingrese un numero: "))
print(f"la variable z vale = {z} y es del tipo {type(z)}")
'''

#EJERCICIO  DE SUMAR NUMEROS
a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = a + b
print(f"El Resultado de la suma entre A y B es: {c}")
