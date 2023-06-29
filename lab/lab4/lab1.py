def calcular_estatura_minima(pacientes):
    estatura_minima = float('inf')  # Establecemos un valor inicial muy alto
    
    for paciente in pacientes:
        estatura = paciente[1]
        if estatura < estatura_minima:
            estatura_minima = estatura
    
    return round(estatura_minima, 1)

pacientes = [["Pedro", 1.78], ["Constanza", 1.56], ["Amanda", 1.62], ["Dario", 1.89], ["Fernanda", 1.67]]
estatura_minima = calcular_estatura_minima(pacientes)
print("Estatura mínima entre los pacientes:", estatura_minima)

def insertar_paciente(pacientes, nuevo_paciente):
    pacientes.append(nuevo_paciente)

nuevo_paciente = ["Ricardo", 1.71]
insertar_paciente(pacientes, nuevo_paciente)
print("Lista de pacientes actualizada:", pacientes)

def buscar_paciente(pacientes, nombre):
    for paciente in pacientes:
        if paciente[0] == nombre:
            print("Nombre:", paciente[0])
            print("Estatura:", paciente[1])
            return
    
    print("No se encuentra el paciente", nombre)

buscar_paciente(pacientes, "Dario")

estatura_minima = calcular_estatura_minima(pacientes)
print("Estatura mínima entre los pacientes:", estatura_minima)

nuevo_paciente = ["Ricardo", 1.71]
insertar_paciente(pacientes, nuevo_paciente)
print("Lista de pacientes actualizada:", pacientes)

buscar_paciente(pacientes, "Dario")
