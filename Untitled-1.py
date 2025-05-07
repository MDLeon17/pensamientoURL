from abc import ABC, abstractmethod

# Clase base abstracta
class Experimento(ABC):
    @abstractmethod
    def realizar_experimento(self):
        pass

# Subclase que hereda de Experimento
class CaidaLibre(Experimento):
    def __init__(self, altura, gravedad):
        self.altura = altura
        self.gravedad = gravedad

    def realizar_experimento(self):
        # Comprobaciones de excepciones
        if self.altura < 0:
            raise ValueError("La altura no puede ser negativa.")
        if self.gravedad == 0:
            raise ValueError("La gravedad no puede ser 0.")
        
        # Cálculo del tiempo de caída
        dato = 2 * self.altura / self.gravedad
        tiempo = dato ** 0.5
        return tiempo

# Bloque principal
try:
    # Pedir al usuario que ingrese los valores
    heigh = float(input("Ingrese la altura en metros: "))
    gravity = float(input("Ingrese la gravedad en m/s^2: "))
    
    # Crear objeto de CaidaLibre
    intento1 = CaidaLibre(heigh, gravity)
    
    # Realizar el experimento y obtener el tiempo de caída
    tiempo_caida = intento1.realizar_experimento()
    
    # Mostrar el resultado
    print(f"El tiempo de caída es: {tiempo_caida:.2f} segundos")
    
except ValueError as e:
    print(f"Error: {e}")
