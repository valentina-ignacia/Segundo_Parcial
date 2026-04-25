print("----------------\n¡Bienvenid@ a Falabella!\n----------------")


while True: 

    # Rut
    rut = input("\nIndique su RUT (sin dígito verificador): ")

    while len(str(rut)) != 8 or rut.isalpha() == True:


        if rut.isalpha() == True:
            print("\n¡El RUT debe contener solo carácteres numéricos!")
            rut = input("Intente nuevamente: ")
        
        elif len(str(rut)) != 8:
            print("\n¡Cantidad de dígitos incorrecta!")
            rut = input("Intente nuevamente: ")

    # Verificador
    verificador = input("\nIndique su dígito verificador: ").upper()

    while len(str(verificador)) != 1 or verificador not in "0123456789K":

        print("\n¡Código verificador debe contener solo un carácter!")
        verificador = input("Intente nuevamente: ").upper()

        

    # Mostrar rut
    
    print(f"\nSu RUT es el: {rut}-{verificador}")

    # Nombre

    nombre = str(input("\nIngrese su nombre y apellido: ")).title().strip()

    nombre_completo = nombre.split()

    while len(nombre_completo) != 2:

        print("\n¡Debe ingresar su nombre y apellido!")
        nombre = input("Intente nuevamente: ").title().strip()
        nombre_completo = nombre.split()

    # Pedir monto de compra y descuentos
    print(f"\n------------------------------\n¡Bienvenid@, {nombre}\n------------------------------")

    monto = int(input("\nIndique el monto de su compra: "))

    if monto > 10000 and monto < 50000:
        print("\n¡Usted tiene disponible un descuento del 10% de su compra!")
        descuento = monto * 0.1
        print(f"Usted tiene un descuento de: ${(descuento)}")
        total = monto - descuento

    elif monto >= 50000:
        print("\n¡Usted tiene disponible un descuento del 20% de su compra!")
        descuento = monto * 0.2
        print(f"Usted tiene un descuento de: ${(descuento)}")
        total = monto - descuento

    else:
        print("\nNo tiene descuento disponible.")
        descuento = 0
        total = monto

    # Boleta final
    print(f"\n-----------------------\nResúmen de su compra\n-----------------------")
    print(F"RUT: {rut}-{verificador}")
    print(f"Nombre: {nombre}")
    print(f"Monto de su compra: ${monto}")
    print(f"Descuento: ${descuento}")
    print(f"Total Compra: ${total}")
    print("-----------------------")

    print("\n¡Gracias por comprar en Falabella Retail!")


    #¿Repetir compra?
    
    while True:
        opcion = input("\n¿Desea realizar otra compra?\n1. Sí\n2. No\n")

        if opcion == "1":
            break

        elif opcion == "2":
            print("\nPrograma finalizado...")
            exit()

        else:
            print("\n¡Opción inválida!\nIntente nuevamente.")
            




