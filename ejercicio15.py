#Ejercicio 15
#El director de una escuela está organizando un viaje de estudios, y requiere determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros, y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de autobuses y lo que debe pagar cada alumno por el viaje.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

alumnos = int(input("Introduce el número de alumnos: "))

if alumnos <= 0:
    print("ERROR: el número de alumnos debe ser mayor que 0")
else:
    if alumnos >= 100:
        por_alumno = 65
        pago_compania = por_alumno * alumnos
    elif alumnos >= 50:
        por_alumno = 70
        pago_compania = por_alumno * alumnos
    elif alumnos >= 30:
        por_alumno = 95
        pago_compania = por_alumno * alumnos
    else:
        pago_compania = 4000
        por_alumno = pago_compania / alumnos

    print(f"Pago a la compañía de autobuses: {pago_compania:.2f} €")
    print(f"Cada alumno debe pagar: {por_alumno:.2f} €")
