import math

class operacion_cientifica:
    def calcular(self):
        print("este metodo debe incluir una subclase")

class raiz_cuadrada(operacion_cientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0:
            print("no hay raiz cuadrada de numero negativos")
            return None
        return math.sqrt(self.numero)

class potencia(operacion_cientifica):
    def __init__(self, base, exponente):
        self.base = base
        self.exponente = exponente

    def calcular(self):
        return self.base ** self.exponente

class log(operacion_cientifica):
    def __init__(self, numero, base=10):
        self.numero = numero
        self.base = base

    def calcular(self):
        if self.numero <= 0:
            raise ValueError("El logaritmo de un número no positivo no está definido")
        return math.log(self.numero, self.base)

class Factorial(operacion_cientifica):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        if self.numero < 0 or not self.numero.is_integer():
            raise ValueError("El factorial solo está definido para números enteros no negativos")
        return math.factorial(int(self.numero))

def ejecutar_operacion(op):
    try:
        resultado = op.calcular()
        if resultado is not None:
            print(f"El resultado de la operación es: {resultado}")
    except ValueError as e:
        print(f"Error: {e}")

def mostrar_menu():
    print("\nOperaciones científicas:")
    print("1. Raíz cuadrada")
    print("2. Potencia")
    print("3. Logaritmo")
    print("4. Factorial")
    print("5. Salir")

def obtener_datos_raiz():
    numero = float(input("Ingrese el número para calcular la raíz cuadrada: "))
    return raiz_cuadrada(numero)

def obtener_datos_potencia():
    base = float(input("Ingrese la base de la potencia: "))
    exponente = float(input("Ingrese el exponente de la potencia: "))
    return potencia(base, exponente)

def obtener_datos_log():
    numero = float(input("Ingrese el número para calcular el logaritmo: "))
    base = float(input("Ingrese la base del logaritmo (por defecto es 10): "))
    return log(numero, base)

def obtener_datos_factorial():
    numero = float(input("Ingrese el número para calcular el factorial: "))
    return Factorial(numero)

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            raiz = obtener_datos_raiz()
            ejecutar_operacion(raiz)
        
        elif opcion == "2":
            potencia_op = obtener_datos_potencia()
            ejecutar_operacion(potencia_op)
        
        elif opcion == "3":
            logaritmo_op = obtener_datos_log()
            ejecutar_operacion(logaritmo_op)
        
        elif opcion == "4":
            factorial_op = obtener_datos_factorial()
            ejecutar_operacion(factorial_op)
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
