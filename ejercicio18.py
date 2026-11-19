#Ejercicio 18
#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

dia = int(input("Introduce el día de la semana (1-7): "))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("ERROR: el número debe estar entre 1 y 7")
