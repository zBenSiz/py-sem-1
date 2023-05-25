"""
BUCLES
"""

#### WHILE (Mientras)

num = 0
while num >= 100:
    print(num)
    num += 2

### WHILE (INFINITOOOOOO)

"""
    while True:
    print(num)    ### Mucho cuidado se recomienda un BREAK
    num += 2   
"""
### WHILE (ELSE/IF)

while num <= 100:
    print(num)
    num += 2
else:
    print("Mi condicion es igualo mayor a 100")

### USO DEL BREAK
"""
while True:
    parametro = input(">")
    if parametro == "exit":  #Desactivado
        break
    else:
        print(parametro)
"""

### USO DEL CONTINUE

num = 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)

### FOR

newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

### ES DECIR, EL FOR:
"""
for <iterador> in <iterable>:
    <Codigo a iterar dentro de este ciclo>
"""