#Ejercicio 12
#Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

anio = int(input("Introduce un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} NO es bisiesto")
