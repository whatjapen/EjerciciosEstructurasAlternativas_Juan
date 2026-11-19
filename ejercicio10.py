#Ejercicio 10
#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique
#•	exteriores
#•	tangentes exteriores
#•	secantes

#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez
import math
print("Circurferencia 1")
x1, y1, r1 = float(input("Introduzca el x1: ")), float(input("Introduzca el y1: ")), float(input("Introduzca el r1: "))
print("Circurferencia 2")
x2, y2, r2 = float(input("Introduzca el x2: ")), float(input("Introduzca el y2: ")), float(input("Introduzca el r2: "))
d = math.hypot(x2-x1, y2-y1)
suma_radios = r1+r2
dif_radios = abs(r1-r2)
if math.isclose(d, suma_radios):
    print ("tangentes exteriores")
elif dif_radios < d < suma_radios:
    print ("secantes")
elif d>suma_radios:
    print ("exteriores")
else:
  print("No es de ningun grupo de (tangentes interiores, interiores o concéntricas)")