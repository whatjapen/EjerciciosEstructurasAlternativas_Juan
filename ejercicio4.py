#Ejercicio 4
#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
numero1,numero2=int(input("Introduzca un numero: ")), int(input("Introduzca otro numero: "))
if numero2==0:
    print ("error, el segundo numero es 0")
else:
    print (numero1, "/", numero2, "=", numero1/numero2)