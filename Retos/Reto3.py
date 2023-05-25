
ciudades = ["Santiago", "Temuco", "Osorno", "Punta Arenas"]
indice_calidad_aire = [134, 99, 245, 50]


indice_min = min(indice_calidad_aire)
indice_max = max(indice_calidad_aire)

print(indice_min)
print(indice_max)

ciudad_minima = ciudades[indice_calidad_aire.index(indice_min)]
ciudad_maxima = ciudades[indice_calidad_aire.index(indice_max)]

print("Ciudad con el índice de calidad del aire más bajo:", ciudad_minima)
print("Ciudad con el índice de calidad del aire más alto:", ciudad_maxima)


categorias = {
    "Buena": (0, 50),
    "Moderada": (51, 100),
    "Dañina a la salud para grupos sensibles": (101, 150),
    "Dañina a la salud": (151, 200),
    "Muy dañina a la salud": (201, 300),
    "Peligrosa": (301, float("inf"))
}


for categoria, rango in categorias.items():
    if indice_min >= rango[0] and indice_min <= rango[1]:
        categoria_minima = categoria
        break


for categoria, rango in categorias.items():
    if indice_max >= rango[0] and indice_max <= rango[1]:
        categoria_maxima = categoria
        break
print("La categoria es la siguiente: ", categorias)

print("Categoría del índice más bajo:", categoria_minima)
print("Categoría del índice más alto:", categoria_maxima)