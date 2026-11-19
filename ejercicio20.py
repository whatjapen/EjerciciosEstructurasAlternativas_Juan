#Ejercicio 20
#Una compañía de transporte internacional tiene servicio en algunos países de América del Norte, América Central, América del Sur, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido. Lo anterior se muestra en la tabla:
#Zona 1 - América del Norte - 24.00 euros/gramo
#Zona 2 - América Central - 20.00 euros/gramo
#Zona 3 - América del Sur - 21.00 euros/gramo
#Zona 4 - Europa - 10.00 euros/gramo
#Zona 5 - Asia - 18.00 euros/gramo
#Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados, esto por cuestiones de logística y de seguridad. Realice un algoritmo para determinar el cobro por la entrega de un paquete o, en su caso, el rechazo de la entrega.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

peso = float(input("Introduce el peso del paquete (kg): "))

if peso <= 0:
    print("ERROR: el peso debe ser mayor que 0")
elif peso > 5:
    print("Entrega rechazada: los paquetes de más de 5 kg no se transportan")
else:
    print("Zonas: 1 = América del Norte, 2 = América Central, 3 = América del Sur, 4 = Europa, 5 = Asia")
    zona = int(input("Introduce la zona de destino (1-5): "))

    if zona == 1:
        costo_gramo = 24
    elif zona == 2:
        costo_gramo = 20
    elif zona == 3:
        costo_gramo = 21
    elif zona == 4:
        costo_gramo = 10
    elif zona == 5:
        costo_gramo = 18
    else:
        costo_gramo = None

    if costo_gramo is None:
        print("ERROR: zona incorrecta")
    else:
        gramos = peso * 1000
        cobro = gramos * costo_gramo
        print(f"El cobro por la entrega es: {cobro:.2f} €")
