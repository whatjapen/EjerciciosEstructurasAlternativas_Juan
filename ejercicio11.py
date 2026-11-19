#Ejercicio 11
#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo. El programa debe determinar que tipo de triangulo es
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez
import math
a,b,c = float(input("Introduzca el lado A: ")),float(input("Introduzca el lado B: ")), float(input("Introduzca el lado C: "))

# Con esta funcion de math puedo ver cual es la hipotenusa en 3 casos diferentes.

pitagoras = (
    math.isclose(a**2 + b**2, c**2)
    or math.isclose(a**2 + c**2, b**2)
    or math.isclose(b**2 + c**2, a**2)
)

if pitagoras:
  print("Triángulo rectángulo")
elif math.isclose(a, b) and math.isclose(b, c):
  print("Triángulo equilátero")
elif math.isclose(a, b) or math.isclose(a, c) or math.isclose(b, c):
  print("Triángulo isósceles")
else:
  print("Triángulo escaleno")