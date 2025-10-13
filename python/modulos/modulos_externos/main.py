#EJEMPLOS

#LIBRERIAS QUE YA ESTAN EN EL CORE DE PYTHON

#libreria para trabajar con fechas y horas
import datetime

hoy = datetime.datetime.now()
print(hoy)

#libreria para trabjar con numeros aleatorios
import random
n = random.randint(1,100)
print(n)

#LIBRERIAS QUE NO ESTAN (LAS TENGO QUE INSTALAR ANTES DE USARLAS)
# SE INSTALAN DE LA SIGUINTE MANERA
# pip install nombre_libreria

'''
import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 6, 8]

# Crear el gráfico
plt.plot(x, y, marker='o')

# Agregar títulos y etiquetas
plt.title("Gráfico rápido en Python")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")

# Mostrar el gráfico
plt.show()

'''

