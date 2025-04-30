class persona:
    def __init__(self, nombre, edad, DPI):
        self.nombre = nombre
        self.edad = edad
        self.DPI = DPI

class estudiante(persona):
    def __init__(self, nombre, edad, DPI, grado, nombre_de_encargado):
        super().__init__(nombre, edad, DPI)
        self.grado = grado
        self.nombre_del_encargado = nombre_de_encargado

    def mostrar_info(self):
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}, DPI: {self.DPI}, Grado: {self.grado}, Encargado: {self.nombre_del_encargado}")

class docente(persona):
    def __init__(self, nombre, edad, DPI, salario, telefono, correo_electronico):
        super().__init__(nombre, edad, DPI)
        self.salario = salario
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def mostrar_info(self):
        print(f"Docente: {self.nombre}, Edad: {self.edad}, DPI: {self.DPI}, Salario: {self.salario}, Teléfono: {self.telefono}, Correo: {self.correo_electronico}")

class administrativo(persona):
    def __init__(self, nombre, edad, DPI, area_designada, grupo_encargado, salario):
        super().__init__(nombre, edad, DPI)
        self.area_designada = area_designada
        self.grupo_encargado = grupo_encargado
        self.salario = salario

    def mostrar_info(self):
        print(f"Administrativo: {self.nombre}, Edad: {self.edad}, DPI: {self.DPI}, Área: {self.area_designada}, Grupo Encargado: {self.grupo_encargado}, Salario: {self.salario}")

# Instancias de ejemplo
est = estudiante("Juan Pérez", 14, "123456789", "8vo", "Carlos Pérez")
doc = docente("María Gómez", 35, "987654321", 5000, "5555-1234", "maria@correo.com")
adm = administrativo("Luis Ramírez", 40, "112233445", "Finanzas", "Grupo A", 4500)

# Menú interactivo
while True:
    print("\n¿Qué clase desea ver?")
    print("1. Estudiante")
    print("2. Docente")
    print("3. Administrativo")
    print("4. Salir")
    
    opcion = input("Ingrese una opción (1-4): ")
    
    if opcion == "1":
        est.mostrar_info()
    elif opcion == "2":
        doc.mostrar_info()
    elif opcion == "3":
        adm.mostrar_info()
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")
