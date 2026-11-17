#Ejercicio 8
#Algoritmo que pida dos números ‘nota’ y ‘edad’ y un carácter ‘sexo’ y muestre el mensaje ‘ACEPTADA’ si la nota es mayor o igual a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’, debe imprimir ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
nota,edad=int(input("Introduzca su nota: ")), int(input("introduzca su edad: "))
sexo = input("M (hombre) o F (mujer)" " Introduzca su sexo: ")

if sexo == "F" and nota>=5 and edad>=18:
    print ("ACEPTADA")
elif sexo == "M" and nota>=5 and edad>=18:
    print("POSIBLE")
else:
    print ("NO ACEPTADA")