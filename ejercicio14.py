#Ejercicio 14
#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
#Fecha: 19/11/2026
#Hecho por: Juan Agea Rodríguez

precio_inicial = float(input("Precio inicial por kilo (€): "))
kilos = float(input("Kilos de uva entregados: "))
tipo = input("Tipo de uva (A/B): ").upper()
tamanio = int(input("Tamaño de la uva (1/2): "))

valido = True

if tipo == "A" and tamanio == 1:
    precio_final = precio_inicial + 0.20
elif tipo == "A" and tamanio == 2:
    precio_final = precio_inicial + 0.30
elif tipo == "B" and tamanio == 1:
    precio_final = precio_inicial - 0.30
elif tipo == "B" and tamanio == 2:
    precio_final = precio_inicial - 0.50
else:
    valido = False

if valido:
    ganancia = precio_final * kilos
    print(f"Precio final por kilo: {precio_final:.2f} €")
    print(f"El productor recibirá: {ganancia:.2f} €")
else:
    print("ERROR: tipo o tamaño incorrectos")
