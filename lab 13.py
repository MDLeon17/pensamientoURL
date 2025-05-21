import copy

# Matriz inicial
matriz = [
    [0,0,0,0,0,0,0,1,1,0],
    [0,1,1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,1,1,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0],
]

def imprimir_tablero(tablero):
    for fila in tablero:
        print(''.join(str(celda) for celda in fila))

def contar_vecinos_lineales(fila, col, matriz):
    vecinos = 0
    if col > 0:
        vecinos += matriz[fila][col - 1]
    if col < len(matriz[0]) - 1:
        vecinos += matriz[fila][col + 1]
    return vecinos

def siguiente_generacion(matriz):
    filas = len(matriz)
    cols = len(matriz[0])
    nueva = copy.deepcopy(matriz)

    for i in range(filas):
        for j in range(cols):
            vecinos = contar_vecinos_lineales(i, j, matriz)
            if matriz[i][j] == 1:
                # Reglas para células vivas
                if vecinos == 1 or vecinos == 2:
                    nueva[i][j] = 1
                else:
                    nueva[i][j] = 0
            else:
                # Reglas para células muertas
                if vecinos == 1:
                    nueva[i][j] = 1
                else:
                    nueva[i][j] = 0
    return nueva

# Simular e imprimir generaciones
print("Generación 0:")
imprimir_tablero(matriz)

generacion_1 = siguiente_generacion(matriz)
print("\nGeneración 1:")
imprimir_tablero(generacion_1)

generacion_2 = siguiente_generacion(generacion_1)
print("\nGeneración 2:")
imprimir_tablero(generacion_2)