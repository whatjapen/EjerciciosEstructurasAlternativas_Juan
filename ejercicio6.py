#Ejercicio 6
#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
entrada = input("Introduzca un texto: ")
if any(letra.isupper() for letra in entrada):
    print("el texto es mayuscula")
else:
    print("el texto es minuscula")