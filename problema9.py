"""
Métodos de Cadenas:
Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.

Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas.
Ejemplo:
- Input: Twitter Output: Twttr
- Input: What's your name? Output: Wht's yr nm?

"""
def esVocal(caracter):
    vocales=['a','e','i','o','u','A','E','I','O','U']
    if caracter in vocales:
        return False #Retorna falso para no guardar las vocales en la nueva cadena
    else:
        return True 

nuevotexto=""

texto=input("Ingrese una cadena de texto: ")

print(texto)

for caracter in texto:
    if esVocal(caracter):
        nuevotexto += caracter

print(nuevotexto)