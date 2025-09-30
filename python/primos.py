N = int(input("Ingresa un número: "))

if N > 1:
	es_primo = True
	#por ejemplo si N es 7 [2,3,4,5,6]
	for i in range(2, N):
		if N % i == 0:
			es_primo = False
			break
	# o es_primo es True, con lo cual nunca se pudo dividir
	# o es_primo es False, con lo cual al menos una vez si se dividio

	if es_primo == True:
		print(N, "es un número primo.")
	else:
		print(N, "NO es un número primo.")
else:
	print(N, "NO es un número primo.")