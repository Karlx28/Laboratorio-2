
#datos de el costo de un articulo vendido y la cantidad de dinero entregado por el cliente 
#El cambio que se debe entregar si sobra
#Cuando lo da exacto
#La cantidad de dinero que falta por pagar si no es exacto
menu = input('''
            Menú de artículos de herramientas    
            1- llave inglesa 
            2- cepillos metálicos 
            3- limas 
            4- destornillador 
            5- taladro 
            Ingresa el articulo que quieres comprar -> ''')
lla = 25
cepi = 10
lim = 6
dest = 8
tal = 45
if menu == "llave inglesa" or menu == "1":
    print("El precio de este producto es de $25")
    d = int(input("Ingrese la cantidad de dinero: "))
    cambio= d - lla
    falta = lla - d
    if d == 25:
        print("Ha entregado lo exacto, muchas gracias")
    elif d > 25:
        print("Usted ha entregado de mas, así que se le dará un cambio de: ", cambio)
    elif d < 25:
        print("Lo sentimos, pero no te alcanza el dinero, te hace falta: ", falta, "dolar/es")
elif menu == "cepillo metálico" or menu == "2":
    print("El precio de este producto es de $10")
    d2 = int(input("Ingrese la cantidad de dinero: "))
    cambio2= d2 - cepi
    falta = cepi - d2
    if d2 == 10:
        print("Ha entregado lo exacto, muchas gracias")
    elif d2 > 10:
        print("Usted ha entregado de mas, así que se le dará un cambio de: ", cambio2)
    elif d2 < 25:
        print("Lo sentimos, pero no te alcanza el dinero, te hace falta: ", falta, "dolar/es")
elif menu == "limas" or menu == "3":
    print("El precio de este producto es de $6") 
    d3 = int(input("Ingrese la cantidad de dinero: "))
    cambio3= d3 - lim
    falta = lim - d3
    if d3 == 6:
        print("Ha entregado lo exacto, muchas gracias")
    elif d3 > 6:
        print("Usted ha entregado de mas, así que se le dará un cambio de: ", cambio3)
    elif d3 < 25:
        print("Lo sentimos, pero no te alcanza el dinero, te hace falta: ", falta, "dolar/es")   
elif menu == "destornillador" or menu == "4":
    print("El precio de este producto es de $8")
    d4 = int(input("Ingrese la cantidad de dinero: "))
    cambio4= d4 - dest
    falta = dest - d4
    if d4 == 8:
        print("Ha entregado lo exacto, muchas gracias")
    elif d4 > 8:
        print("Usted ha entregado de mas, así que se le dará un cambio de: ", cambio4)
    elif d4 < 25:
        print("Lo sentimos, pero no te alcanza el dinero, te hace falta: ", falta, "dolar/es")
elif menu == "taladro" or menu == "5":
    print("El precio de este producto es de $45")
    d5 = int(input("Ingrese la cantidad de dinero: "))
    cambio5= d5 - tal
    falta = tal - d5
    if d5 == 45:
        print("Ha entregado lo exacto, muchas gracias")
    elif d5 > 45:
        print("Usted ha entregado de mas, así que se le dará un cambio de: ", cambio5)
    elif d5 < 25:
        print("Lo sentimos, pero no te alcanza el dinero, te hace falta: ", falta, "dolar/es")
else: 
    print("El dato que ingresaste no se encuentra")

