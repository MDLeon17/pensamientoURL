
array = int(input("ingrese el tamaño del array: "))
multiplo = int(input("ingrese el multiplo: "))
array1 = []
for i in range(1, array+1):
    array1.append(i*multiplo)

print(array1)    

# Ejercicio 2
nombres = []
NumNombres = []

recorrido = int(input("ingrese el numero de datos"))
for name in range (1, recorrido + 1):
    name = input(f"ingrese el nombre {name} ") 
    nombres.append(name)
    NumNombres.append(len(nombres))

print (NumNombres,  nombres )


