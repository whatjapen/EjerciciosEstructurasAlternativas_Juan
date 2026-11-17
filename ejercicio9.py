#Ejercicio 9
#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor)
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
num1,num2,num3= input("Introduzca 1º numero: "), input("introduzca 2º numero: "), input("introduzca 3º numero: ")
nums=type[num1,num2,num3]
if num1>nums and num2>num3:
    print (num1, num2, num3)
elif num3>nums and num2>num1:
    print (num3, num2, num1)
elif num2>nums and num3>num1:
    print (num2, num3, num1)
else:
    print(num3, num1, num2)
## POR HACER