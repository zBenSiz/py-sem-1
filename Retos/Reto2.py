###Algoritmo
nombre_estudiante= input("¿Cual es el nombre del estudiante? ")
asignatura= input("Elija la Asignatura ")
notalab1= float(input("Ingrese la primera nota "))
notalab2=float(input("Ingrese la segunda nota "))


estudiante= {
    "Nombre":nombre_estudiante,
    "Asignatura":asignatura,
    "Nota-lab-1":notalab1,
    "Nota-lab-2":notalab2,
}
prom= notalab1*0.30
prom2= notalab2*0.70
prom_final=float(prom+prom2 / 2)

print("Informacion del estudiante: ", estudiante)
print(f"Promedio Final:  {prom_final:.1f}")
