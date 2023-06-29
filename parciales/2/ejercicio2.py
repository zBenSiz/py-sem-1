"""Calcular la media de calificaciones de la asignatura de Programación. Deducir cuántas son
más altas que la media y cuántas más bajas que dicha media. Se solicita un mínimo de 10
notas. Estas calificaciones se ingresarán por teclado y no se permite notas inferiores a 1.0 ni
mayores a 7.0"""

num_calificaciones = int(input("Ingrese el número de calificaciones: "))

if num_calificaciones < 10:
    print("Debe ingresar al menos 10 calificaciones.")
    exit()

calificaciones = []
suma_calificaciones = 0


for i in range(num_calificaciones):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    if calificacion < 1.0 or calificacion > 7.0:
        print("La calificación debe estar entre 1.0 y 7.0.")
        exit()
    calificaciones.append(calificacion)
    suma_calificaciones += calificacion


media = suma_calificaciones / num_calificaciones

mas_altas = 0
mas_bajas = 0

for calificacion in calificaciones:
    if calificacion > media:
        mas_altas += 1
    elif calificacion < media:
        mas_bajas += 1

print("Media de calificaciones:", media)
print("Calificaciones más altas que la media:", mas_altas)
print("Calificaciones más bajas que la media:", mas_bajas)
