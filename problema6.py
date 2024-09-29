""""
Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.

"""
lista_fibonacci=[0,1]

while True:
    siguientenumero = lista_fibonacci[-1]+ lista_fibonacci[-2]
    if siguientenumero>50:
        break
    lista_fibonacci.append(siguientenumero)

print(lista_fibonacci)