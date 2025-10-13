
from datetime import date
from dateutil.relativedelta import relativedelta
dia = int(input("Ingresar Día de nacimiento: "))
mes = int(input("Ingresar Mes de nacimiento: "))
anio = int(input("Ingresar Año de nacimiento: "))
nacimiento = date(anio, mes, dia)
hoy = date.today()
edad = relativedelta(hoy, nacimiento)
print(f"\nLa edad exacta es: {edad.years} años, {edad.months} meses y {edad.days} días.")

import datetime
import calendar

print("Calcular tu edad exacta (Año, Mes, Día)")
dia = int(input("Ingrese el día de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
año = int(input("Ingrese el año de nacimiento: "))

def calcular_edad(a, b, c):
	nacimiento = datetime.date(c, b, a)
	hoy = datetime.date.today()

	años = hoy.year - nacimiento.year
	if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
		años -= 1

	meses = hoy.month - nacimiento.month
	if hoy.day < nacimiento.day:
		meses -= 1
	if meses < 0:
		meses += 12

	if hoy.day >= nacimiento.day:
		dias = hoy.day - nacimiento.day
	else:
		mes_anterior = hoy.month - 1 or 12
		año_anterior = hoy.year if hoy.month != 1 else hoy.year - 1
		dias_en_mes_anterior = calendar.monthrange(año_anterior, mes_anterior)[1]
		dias = hoy.day + dias_en_mes_anterior - nacimiento.day

	print(f"Tienes {años} años, {meses} meses y {dias} días")

calcular_edad(dia, mes, año)
