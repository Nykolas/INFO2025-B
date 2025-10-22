class Vehiculo:
	def __init__(self, marca, color, velocidad_maxima):
		self.__marca = marca.capitalize()
		self.__color = color
		self.__velocidad_maxima = velocidad_maxima
	def get_marca(self):
		return self.__marca
	def get_color(self):
		return self.__color
	def get_velocidad_maxima(self):
		return self.__velocidad_maxima
	def set_marca(self, marca):
		self.__marca = marca
	def set_color(self, color):
		self.__color = color
	def set_velocidad_maxima(self, velocidad):
		self.__velocidad_maxima = velocidad

	def mostrar_info(self):
		print(f" Marca: {self.__marca}")
		print(f" Color: {self.__color}")
		print(f" Velocidad Máxima: {self.__velocidad_maxima} km/h")

class Auto(Vehiculo):
	def __init__(self, marca, color, velocidad_maxima, cantidad_puertas):
		#super llama al padre
		super().__init__(marca,color,velocidad_maxima)
		self.__cantidad_puertas = cantidad_puertas
	def get_cantidad_puertas(self):
		return self.__cantidad_puertas
	def set_cantidad_puertas(self, puertas):
		self.__cantidad_puertas = puertas
	def mostrar_info(self):
		print(f"\nAuto:")
		super().mostrar_info()
		print(f" Puertas: {self.__cantidad_puertas}")

class Moto(Vehiculo):
	def __init__(self, marca, color, velocidad_maxima, cilindrada):
		super().__init__(marca,color,velocidad_maxima)
		self.__cilindrada = cilindrada
	def get_cilindrada(self):
		return self.__cilindrada
	def set_cilindrada(self, cilindrada):
		self.__cilindrada = cilindrada
	def mostrar_info(self):
		print(f"\nMoto:")
		super().mostrar_info()
		print(f" Cilindrada: {self.__cilindrada} cc")
