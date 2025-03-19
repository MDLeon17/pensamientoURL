saldo = 3000
attempt = 2
while True:  
    print("Que accion desea realizar el dia de hoy?")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("0. Salir")
    opcion = int(input())  
    if opcion == 0:
        break
    elif opcion == 1:
        print("su saldo es: ", saldo)
    elif opcion == 2:
        print("cuanto desea retirar?")
        print("usted tiene un saldo de: ", saldo, "ingrese cuanto desea retirar")  
        print("si desea retirar todo su saldo, ingrese 1")
        retiro = int(input())
        if retiro > saldo:
            print("saldo insuficiente")
            print("intentos restantes: ", attempt)
            attempt -= 1
            if attempt == -1:
                print("ha agotado sus intentos")
                break
        elif retiro == 1:
            print("se retiraron todos los fondos con un total de ", saldo)
        elif retiro < saldo:
            saldo -= retiro
            print("su saldo actual es: ", saldo)
        else:  
            print("se retiraron todos los fondos con un total de ", saldo)
            saldo = 0  
    else:
        print("Opcion invalida, intente de nuevo.")  