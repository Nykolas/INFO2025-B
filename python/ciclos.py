'''
#ciclo while (mientras)
x = 1
while x < 10:
	print(x)
	x = x + 1 
	
print("-------------")
# ciclo para
# el range [0,1,2,3,4,5,6,7,8,9]
# range(vi,vf,incremento)
#si no especifico, vi e incremento,
#por defecto es 0 y el incremento de a 1
for i in range(1,10,2):
	print(i)
'''

#Ciclo que se ejecuta mientras el usuario asi lo quiera
seguir = "si"
while seguir == "si":
	print("seguimos.....")
	seguir = input("quiere seguir? ")