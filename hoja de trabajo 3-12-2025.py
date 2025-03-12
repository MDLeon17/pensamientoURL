habitantes = int(input("Ingrese la cantidad de habitantes: "))
consumoa = int (input("Ingrese el consumo de agua en metros cubicos: "))
precio = 0
if consumoa < 15:
    precio = 5
elif consumoa >= 15 and consumoa < 30 and habitantes == 3:
    precio = 4.5
elif consumoa >= 15 and consumoa < 30 and habitantes > 3 and habitantes < 5:
    precio = 4 
elif consumoa >= 15 and consumoa < 30 and habitantes < 3:
    precio = 5
elif consumoa >= 30 and habitantes >= 5 and habitantes % 2 != 0:
    precio = 3.5
elif consumoa >= 30 and habitantes >= 5 and habitantes % 2 == 0:
    precio = 4
elif consumoa >= 30 and habitantes < 5:
    precio = 4.2

print("El precio a pagar es de: ", precio * consumoa)



año = int(input("Ingrese el año del vehiculo: "))
placa = int(input("Ingrese el numero de placa del vehiculo: "))
if año >= 2001 and año < 2999:
    if placa % 2 == 0:
        print("su vehiculo no puede circular los dias viernes")
    else:
        print("su vehiculo no puede circular los dias lunes")
        print("su vehiculo no puede circular hasta medio dia los sabados")
elif año < 2001 and año > 1900:
    print("su vehiculo no puede circular hasta que le haga mantenimiento")
else:
    print("año invalido")
