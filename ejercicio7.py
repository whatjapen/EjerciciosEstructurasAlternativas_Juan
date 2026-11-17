#Ejercicio 7
#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente.
#Fecha: 17/11/2026
#Hecho por: Juan Agea Rodríguez
base,exponente = int(input("base: ")), int(input("exponente: "))
potencia = (base**exponente)
if exponente>0:
    print ("resultado: ", potencia)
elif exponente==0:
    print ("resultado: 1")
elif exponente<0:
    potencianegativa = (base ** (-1*exponente))
    print ("resultado: ", 1/potencianegativa)