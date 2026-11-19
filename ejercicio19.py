#Ejercicio 19
#Escribe un programa que pida un número entero entre uno y doce e imprima el número de días que tiene el mes correspondiente.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

mes = int(input("Introduce un número de mes (1-12): "))

if mes < 1 or mes > 12:
    print("ERROR: el mes debe estar entre 1 y 12")
elif mes == 2:
    print("El mes tiene 28 días (29 si el año es bisiesto)")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("El mes tiene 30 días")
else:
    print("El mes tiene 31 días")
