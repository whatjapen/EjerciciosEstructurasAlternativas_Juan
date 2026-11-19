#Ejercicio 13
#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

bisiesto = (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

if mes < 1 or mes > 12 or dia < 1:
    correcta = False
elif mes == 2:
    if bisiesto:
        correcta = dia <= 29
    else:
        correcta = dia <= 28
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    correcta = dia <= 30
else:
    correcta = dia <= 31

if correcta:
    print("La fecha es correcta")
else:
    print("La fecha NO es correcta")
