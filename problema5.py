
"""
Problema 5:
Escribe un programa que encuentre la suma de todos los números primos menores que 100.
"""
lista_primos=[]
from pprint import pprint
def numeroprimo(numero):
    for i in range(2,numero):
        if numero % i == 0:
            return False
        else:
            return True
    return True

for num in range(2,101):
    if numeroprimo(num):
        lista_primos.append(num)
suma_primos= sum(lista_primos)


print(lista_primos)

print("Suma de primos: ", suma_primos)

