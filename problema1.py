"""
Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).

"""

lista=[]
from pprint import pprint
for numero in range(1500,2701):
    if numero % 7 == 0 and numero % 5 == 0:
        lista.append(numero)
    
pprint(lista)
