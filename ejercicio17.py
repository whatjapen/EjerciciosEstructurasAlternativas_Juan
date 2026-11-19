#Ejercicio 17
#Realiza un programa que pida por teclado el resultado (dato entero) obtenido al lanzar un dado de seis caras y muestre por pantalla el número en letras (dato cadena) de la cara opuesta al resultado obtenido.
#- Nota 1: En las caras opuestas de un dado de seis caras están los números: 1-6, 2-5 y 3-4.
#- Nota 2: Si el número del dado introducido es menor que 1 o mayor que 6, se mostrará el mensaje: “ERROR: número incorrecto.”.
#Ejemplo:
#Introduzca número del dado: 5
#En la cara opuesta está el "dos".
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

dado = int(input("Introduzca número del dado: "))

if dado < 1 or dado > 6:
    print("ERROR: número incorrecto.")
else:
    opuesta = 7 - dado

    if opuesta == 1:
        letras = "uno"
    elif opuesta == 2:
        letras = "dos"
    elif opuesta == 3:
        letras = "tres"
    elif opuesta == 4:
        letras = "cuatro"
    elif opuesta == 5:
        letras = "cinco"
    else:
        letras = "seis"

    print(f'En la cara opuesta está el "{letras}".')
