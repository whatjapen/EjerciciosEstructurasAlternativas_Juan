#Ejercicio 16
#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

minutos = int(input("Duración de la llamada (minutos): "))
dia = int(input("Día de la semana (1 = lunes ... 7 = domingo): "))

if minutos < 0 or dia < 1 or dia > 7:
    print("ERROR: datos incorrectos")
else:
    # Coste de la llamada según el tiempo
    if minutos <= 5:
        coste = minutos * 1.00
    elif minutos <= 8:
        coste = 5 * 1.00 + (minutos - 5) * 0.80
    elif minutos <= 10:
        coste = 5 * 1.00 + 3 * 0.80 + (minutos - 8) * 0.70
    else:
        coste = 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50

    # Impuesto según el día y el turno
    porcentaje = None
    if dia == 7:
        porcentaje = 0.03
    else:
        turno = input("Turno (M = mañana, T = tarde): ").upper()
        if turno == "M":
            porcentaje = 0.15
        elif turno == "T":
            porcentaje = 0.10

    if porcentaje is None:
        print("ERROR: turno incorrecto")
    else:
        impuesto = coste * porcentaje
        total = coste + impuesto
        print(f"Coste de la llamada: {coste:.2f} €")
        print(f"Impuesto ({porcentaje * 100:.0f} %): {impuesto:.2f} €")
        print(f"Total a pagar: {total:.2f} €")
