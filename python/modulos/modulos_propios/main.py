#para importar (osea traer funciones que estan en otro archivoo o modulo)
#existen varias maneras.

#1) importar todo el archivo directamente
#en este ejemplo, funciona siempre y cuando ambos archivos esten
#en la misma carpeta
import funciones_propias
#como usar si importo de esta manera
res = funciones_propias.sumar(6,6)
print(res)

#2) importar todas las funciones que estan en el archivo
from funciones_propias import *
res = sumar(6,6)
print(res)
res = multiplicar(6,6)
print(res)
res = restar(6,6)
print(res)
#3)importar la/las funciones especificas que necesito
from funciones_propias import sumar,multiplicar
res = sumar(6,6)
print(res)
res = multiplicar(6,6)
print(res)
#esto da error porque no imprte restar
res = restar(6,6)
print(res)


