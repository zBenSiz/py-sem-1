a = [10, 9, 12, 15, 18]
b = [21, 8, 15, 3, 12]

concatenada = a + b
print("Lista concatenada:", concatenada)
concatenada.insert(1, 30)
print("Lista con el número 30 agregado:", concatenada)
concatenada.sort()
print("Lista ordenada:", concatenada)
concatenada.append([4, 5, 6])
print("Lista con [4, 5, 6] insertada:", concatenada)
suma = sum(concatenada[:concatenada.index([4, 5, 6])])
print("Suma total de la lista:", suma)

longitud = len(concatenada)
media = suma_total / longitud

if longitud % 2 == 0:
    mediana = (concatenada[longitud // 2 - 1] + concatenada[longitud // 2]) / 2
else:
    mediana = concatenada[longitud // 2]

print("Media:", media)
print("Mediana:", mediana)
