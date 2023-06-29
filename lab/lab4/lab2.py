
### ! ###

def encontrar_palabra_mas_larga(lista):
    palabra_mas_larga = ""
    for palabra in lista:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

a = ["Rojo", "Verde", "Celeste", "Violeta"]
palabra_mas_larga_a = encontrar_palabra_mas_larga(a)
print("Palabra con más caracteres en la lista a:", palabra_mas_larga_a)

#### 2 ####

def encontrar_palabra_mas_corta(lista):
    palabra_mas_corta = lista[0]
    for palabra in lista:
        if len(palabra) < len(palabra_mas_corta):
            palabra_mas_corta = palabra
    return palabra_mas_corta

b = ["Osorno", "Puerto Montt", "Puerto Varas", "Valdivia"]
palabra_mas_corta_b = encontrar_palabra_mas_corta(b)
print("Palabra con menos caracteres en la lista b:", palabra_mas_corta_b)

#### 3 ####

def concatenar_listas(lista1, lista2):
    return lista1 + lista2

concatenacion = concatenar_listas(a, b)
print("Lista concatenada:", concatenacion)

#### 4 ####

def convertir_a_mayusculas(lista):
    lista_mayusculas = []
    for palabra in lista:
        lista_mayusculas.append(palabra.upper())
    return lista_mayusculas

a_en_mayusculas = convertir_a_mayusculas(a)
b_en_mayusculas = convertir_a_mayusculas(b)
print("Lista a en mayúsculas:", a_en_mayusculas)
print("Lista b en mayúsculas:", b_en_mayusculas)

#### 5 ####

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada

a_ordenada = ordenar_lista(a)
b_ordenada = ordenar_lista(b)
print("Lista a ordenada:", a_ordenada)
print("Lista b ordenada:", b_ordenada)
