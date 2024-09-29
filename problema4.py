"""
Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{
Alumno: Juan,
Notas: [10, 12, 15]
}
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.
Nota:
El uso de listas con diccionarios le será de utilidad.
"""
from pprint import pprint
lista_alumnos=[]


numero_alumnos=int(input("Ingrese cuantos alumnos desea ingresar: "))


for i in range(numero_alumnos):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    nota = []

    for j in range(3):
        calificacion= input(f"Ingrese la nota {j+1}: ")
        nota.append(calificacion)

    alumno = {
        "Nombre": nombre,
        "Notas": nota
    }

    lista_alumnos.append(alumno)

    print("\nListado completo de alumnos y sus calificaciones:")
for alumno in lista_alumnos:
   pprint(lista_alumnos)
     