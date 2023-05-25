###CLASE 4#####
"""
Condicionales
"""


#### IF
edad= 19
if edad >= 18: ### Siempre :
	print("Eres mayor de edad")

    #### ES IMPORTANTE IDENTAR

edad = 19
if edad >= 18:
	print("Eres mayor de edad")
print("Este print esta fuera del if")

###ELSE

edad= 19
if edad >= 18:
	print("eres mayor de edad")
else:
	print("Eres menor de edad")

###ELIF

edad = 66

if edad >= 18 and edad < 65:
	print("Eres mayor de edad")
elif edad >= 65:
	print("Eres un adulto mayor")
else:
	print("Eres menor de edad")

### OPERADOR TERNARIO ####

edad = 19
print("Usted puede Votar" if edad >= 18 else "Usted no puede votar")


