print("Algoritmo para saber si el Numero es Par o Impar")
num=int(input("Ingrese un numero: "))

if num % 2 == 0:
    print("Es un numero par")
else:
    print("Es un numero impar")
#####

if num <= 2:
    print("Es un numero primo ")
for i in range(2, int(num**0.5)+ 1):
    if num % i ==0:
        print("No Es un numero primo ")
        break



######
if num > 50:
    print("Es mayor a 50")
else:
    print("Es menor o igual a 50 ")