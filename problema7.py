"""
Problema 7:
Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
(excluyendo el propio número).
Ejemplo Identificar número perfecto:
Número perfecto: 6
● Divisores propios: 1, 2, 3
● Suma de los divisores propios: 1 + 2 + 3 = 6
"""


def esPerfecto(numero):
    listado_divisores = []
    for i in range(1,numero):    
        if numero % i == 0:
         listado_divisores.append(i)
    if numero == sum(listado_divisores):
       return True
    else:
       return False
    
lista_perfectos=[]

for num in range(1,1001):
    if esPerfecto(num):
        lista_perfectos.append(num)


print(lista_perfectos)

