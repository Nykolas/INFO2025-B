from clases import Auto, Moto

print("=== Crear un Auto ===")
marca_auto = input("Marca del auto: ")
color_auto = input("Color del auto: ")
velocidad_auto = int(input("Velocidad máxima del auto: "))
puertas_auto = int(input("Cantidad de puertas: "))

auto1 = Auto(marca_auto, color_auto, velocidad_auto, puertas_auto)
auto1.mostrar_info()

print("\n=== Crear una Moto ===")
marca_moto = input("Marca de la moto: ")
color_moto = input("Color de la moto: ")
velocidad_moto = int(input("Velocidad máxima de la moto: "))
cilindrada_moto = int(input("Cilindrada (en cc): "))

moto1 = Moto(marca_moto, color_moto, velocidad_moto, cilindrada_moto)
moto1.mostrar_info()