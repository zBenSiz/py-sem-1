"""
Construir un algoritmo que permita generar enteros de 3 en 3 comenzado por el 2 hasta el
valor máximo que será menor que 30. Calcular la suma de los enteros generados que sean
divisibles por 5, y la suma de los enteros generados que sean impares.

"""
num=2
while num<30:
    print(num)
    num+=3 

print()

num = 2
suma_divisibles_5 = 0
suma_impares = 0

while num < 30:
    if num % 5 == 0:
        suma_divisibles_5 += num
    if num % 2 != 0:
        suma_impares += num
    num += 3

print("La suma de los enteros divisibles por 5 es:", suma_divisibles_5)
print("La suma de los enteros impares es:", suma_impares)

