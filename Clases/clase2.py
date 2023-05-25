###CLASE 2

#Que hacen estas funciones?
print(list("python"))
print(list(range(10)))
print("\n")

#TUPLAS (no mutables)
newtupla= tuple()
grupo1= ("Daniel","Cristian","Felipe",200,100,"Daniel")
print("######TUPLAS######")
print(type(grupo1))

#Seleccionar el primer Estudiante o cosa
print(grupo1[0])

#Index = Muestra la posicion de los elementos seleccionados

#Reemplazar o cambiar un valor
grupo1[0]= "Constanza"
print(grupo1)

#Se pueden sumar las tuplas
#no

#Obteniendo un trozo de la Tupla
grupo2=("pedro",100,"Felipe","diego",2020,"alejandra")
print("Trozo de la Tupla",grupo2[0:3])

#como modificar una tupla?
grupo1= list(grupo1)
print("la tupla ahora es de tipo:",type(grupo1),"\n")
print("\n")

#SETS (Conjuntos) - Estructura Fija
#Como iniciar

conjunto_vacio= set()
conjunto_vacio1={} #dict o set?
print(type(conjunto_vacio1)) #aqui se ve el tipo
conjunto_colores= set({"azul","rojo","verde"})
conjunto_animal={"gato","perro","loro"}
#asi se llama
print("Los siguientes colores son:",conjunto_colores)
print("los siguientes animales son:",conjunto_animal)

print(conjunto_animal[0])
conjunto_colores.add("Celecte")
print("Colores actualizados con",conjunto_colores)
