"""
Se cuenta con dos sets, los cuales contienen precios de productos: (40 Puntos)
Set 1 = {100, 250, 300, 1000}
Set 2 = {150, 250, 500, 1000}
A) Verificar si el valor 100 está en ambos sets
B) Comprobar si al menos el valor 500 o 700 está en alguno de los sets
C) Elevar a 3 todos los valores dentro de los sets
D) Unir ambos sets en uno solo
"""

Set1 = {100, 250, 300, 1000}
Set2 = {150, 250, 500, 1000}

print("Verificar si el valor 100 está en ambos sets")
print()

if 100 in Set1:
    print("Se encuentra 100 en el primer Set")
else:
    print("100 No se encuentra en el primer Set")
if 100 in Set2:
    print("Se encuentra 100 en el segundo Set")
else:
    print("100 No se encuentra en Segundo Set")

print("Comprobar si al menos el valor 500 o 700 está en alguno de los sets")
print()

print("SET 1")
print()
if 500 in Set1:
    print("Se encuentra el 500 en el Set 1")
else:
    print("No se encuentra el 500 en el Set 1")
    if 700 in Set1:
        print("Se encuentra el 700 en el Set 1")
    else:
        print("No se encuentra el 700 en el Set 1 ")

print("SET 2")
print()
if 500 in Set2:
    print("Se encuentra el 500 en el Set 2")
else:
    print("No se encuentra el 500 en el Set 2")
    if 700 in Set2:
        print("Se encuentra el 700 en el Set 2")
    else:
        print("No se encuentra el 700 en el Set 2 ")

print()
print("Elevar a 3 todos los valores dentro de los sets")
print()

Elevado1 = {x ** 3 for x in Set1}
Elevado2 = {x ** 3 for x in Set2}

print(Elevado1)
print(Elevado2)

print("D) Unir ambos sets en uno solo")
print(Set1.union(Set2))



