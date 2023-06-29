def longitud(frase):
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario





frase = input("Ingresar tu frase por favor: ")
resultado = longitud(frase)
print(resultado)