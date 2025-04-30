class Animal:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.peso = peso
        self.edad = edad

class gato(Animal):
    def __init__(self, nombre, edad, peso, tamaño, pelaje, personalidad):
        super().__init__(nombre, edad, peso)
        self.tamaño = tamaño
        self.pelaje = pelaje
        self.personalidad = personalidad

    def mostrar_info(self):
        print(f"Gato: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}kg, Tamaño: {self.tamaño}, Pelaje: {self.pelaje}, Personalidad: {self.personalidad}")

class perro(Animal):
    def __init__(self, nombre, edad, peso, tamaño, temperamento, pelaje):
        super().__init__(nombre, edad, peso)
        self.tamaño = tamaño
        self.temperamento = temperamento
        self.pelaje = pelaje

    def mostrar_info(self):
        print(f"Perro: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}kg, Tamaño: {self.tamaño}, Temperamento: {self.temperamento}, Pelaje: {self.pelaje}")

class ave(Animal):
    def __init__(self, nombre, edad, peso, Tpico, Capacidad_de_vuelo, tipo_de_patas):
        super().__init__(nombre, edad, peso)
        self.Tpico = Tpico
        self.Capacidad_de_vuelo = Capacidad_de_vuelo
        self.tipo_de_patas = tipo_de_patas

    def mostrar_info(self):
        print(f"Ave: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}kg, Pico: {self.Tpico}, Vuelo: {self.Capacidad_de_vuelo}, Patas: {self.tipo_de_patas}")

class reptil(Animal):
    def __init__(self, nombre, edad, peso, Tipo_de_piel, Habitat, Alimentacion):
        super().__init__(nombre, edad, peso)
        self.Tipo_de_piel = Tipo_de_piel
        self.habitat = Habitat
        self.alimentacion = Alimentacion

    def mostrar_info(self):
        print(f"Reptil: {self.nombre}, Edad: {self.edad}, Peso: {self.peso}kg, Piel: {self.Tipo_de_piel}, Hábitat: {self.habitat}, Alimentación: {self.alimentacion}")


while True:
    print("\n¿Qué clase desea ver?")
    print("1. Gato")
    print("2. Perro")
    print("3. Ave")
    print("4. Reptil")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        g = gato("Michi", 2, 4.5, "mediano", "corto", "juguetón")
        g.mostrar_info()
    elif opcion == "2":
        p = perro("Firulais", 5, 20.0, "grande", "leal", "largo")
        p.mostrar_info()
    elif opcion == "3":
        a = ave("Loro", 1, 0.3, "curvo", "buena", "delgadas")
        a.mostrar_info()
    elif opcion == "4":
        r = reptil("Iguana", 3, 1.2, "escamosa", "selva", "herbívoro")
        r.mostrar_info()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
