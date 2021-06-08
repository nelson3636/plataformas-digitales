"""
STRING 

"""

esto_es_una_string="hola, esto es una prueba"
esto_es_otra_string="mundo"
print(esto_es_una_string + " " +esto_es_otra_string)

#solo mayuscula las variables upper

print(esto_es_una_string.upper())

#solo minuscula
print(esto_es_una_string.lower())

#solo la primera letra de la primera palabra en mayuscula
print(esto_es_una_string.capitalize())

#las primeras letras de todas las palabras en mayuscula
print(esto_es_una_string.title())

#me dice la longitud de cuantas letras tiene
print(len(esto_es_una_string))

#buscar un caracter y muestra su ubicacion
print(esto_es_una_string.find("e"))

#imprimir solo la primera letra [inicio:fin:el incremento] incremento es por ejemplo si  pone 2 significa que muestra de dos en dos 
print(esto_es_una_string[0:2])
print(esto_es_una_string[0:1])
print(esto_es_una_string[6:10])

#radar: de atras para delante
print(esto_es_una_string[::-1])