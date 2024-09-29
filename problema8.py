"""
Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.

"""

def Factorial(num):
    if num<0:
        return "No se puede sacar factorial a un negativo"
    elif num == 0:
        return 1
    prod=1
    for i in range(1,num+1):
        prod*= i
    return prod

    
numero = int(input("Ingrese un numero: "))
resultado = Factorial(numero)
print(f"El factorial de {numero} es {Factorial(numero)}.")