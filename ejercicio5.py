#Ejercicio 5
#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
usuario=input("Introduzca su usuario: ")
contrasena=input("introduzca su contraseña: ")
if usuario=="pepe" and contrasena=="asdasd":
    print ("Has entrado al sistema")
else:
    print ("Usuario o contraseña incorrecta")