#Clase 1
# #tipos de datos 
estatura= 1.70
peso= 70.5
edad= 29
print(peso)
print("transformar el valor real a entero:",int(peso))
print("transformar de entero a decimal",float(edad))

imc= peso/ (estatura**2)
print("mi imc es: ",{imc})


asignatura= 'programacion'
carrera= "IngCivilInformatica"
print("la asignatura de:",asignatura,"corresponde a la carrera de ", carrera)

print("Cantidad de caracteres de la palabra", asignatura, "es de",len(asignatura))
print("Cantidad de caracteres de la palabra", carrera, "es de",len(carrera))

#Booleanos
ampolleta= False
interruptor= True

print(ampolleta,interruptor)
print("Lavariable ampolleta es de tipo",type(ampolleta) )

print(bool(0))
print(bool(" "))
print(bool(None))
print(bool("True"))
print(bool(1))

print("LISTA")

nueva_lista= list()
otra_lista= list
print("esta lista esta vacia", nueva_lista)
print(type(nueva_lista))
 ## declarando 3 lista diferentes

estudiantes=["Matias","Marco","Cristobal","Sebastian","Marco"]
num=[1,2,3,4,5,6,1]
lenguaje=["Python"]

data= ["osorno"]
listamixta=["felipe", 100, True]

print("Lista de estudiantes; ", estudiantes)
print("lista de numeros: ",num)
print("Lista de un elemento ",lenguaje)
print("esta lista es mixta: ", listamixta)
print("esto igual es una lista: ",data )
print(estudiantes.count("Marco"))
print(num.count(1))

Lenguaje= ["Javascript"]
print("Nuevo Valor del arreglo de un elemeto", lenguaje)

#como elijo a uno de los estudiantes
print(estudiantes[0])
print(estudiantes[3])
print(estudiantes[0])#incorrecto
print("Posicion -2",estudiantes[-2])#se devuelve es a la inversa