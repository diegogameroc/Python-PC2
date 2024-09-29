"""
Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.
Ejemplo:
“Desea ingresar un número?”: SI
“Ingrese el número:” 5
“¿Desea ingresar un número?”: SI
“Ingrese el número: ” 7
……
“Desea ingresar un número?”: NO
Números ingresados: [ 5,7, 6, 7, 8, 9, 1, 2, 3, 4]
Cantidad de números pares: 5
Cantidad de números impares: 4
Nota:
- Quizás a manera de ayuda el uso de una lista le sea de utilidad.
- El empleo de break sobre condiciones while también le serán de utilidad.

"""

lista_num=[]
listado_par=[]
listado_impar=[]
contpares=0
contimpares=0

while True:
    decic=input("Desea ingresar un numero?: ")
    if decic=="SI":
        num=int(input("Ingrese el numero: "))
        lista_num.append(num)
    elif decic=="NO":
        break;

for num in lista_num:
    if num % 2 == 0:
        contpares+=1
        listado_par.append(num)
        
for num in lista_num:
    if num % 2 == 1:
        contimpares+=1
        listado_impar.append(num)


print(f"Numeros ingresados: {lista_num}")
#print(listado_par)
print(f"Los numeros pares son {listado_par} y la cantidad es {contpares}")
print(f"Los numeros impares son {listado_impar} y la cantidad es {contimpares}")