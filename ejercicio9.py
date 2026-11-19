#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
num1, num2, num3 = int(input("Introduzca 1° numero: ")), int(input("introduzca 2° numero: ")), int(input("introduzca 3° numero: "))
if num1 >= num2 >= num3:
    print(num1, num2, num3)
elif num3 >= num2 >= num1:
    print(num3, num2, num1)
elif num2 >= num3 >= num1:
    print(num2, num3, num1)
elif num3 >= num1 >= num2:
    print(num3, num1, num2)
elif num1 >= num3 >= num2:
    print(num1, num3, num2)
elif num2 >= num1 >= num3:
    print(num2, num1, num3)
else:
    print("Error")