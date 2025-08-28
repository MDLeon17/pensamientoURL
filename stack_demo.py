"""Demostración de stack mediante llamadas anidadas a funciones.
Cada función define una variable local y la imprime junto con el nombre de la función.
"""

def funcion5():
    quinta_variable = "valor en funcion5"
    print("funcion5 -> quinta_variable:", quinta_variable)


def funcion4():
    cuarta_variable = "valor en funcion4"
    print("funcion4 -> cuarta_variable:", cuarta_variable)
    funcion5()


def funcion3():
    tercera_variable = "valor en funcion3"
    print("funcion3 -> tercera_variable:", tercera_variable)
    funcion4()


def funcion2():
    segunda_variable = "valor en funcion2"
    print("funcion2 -> segunda_variable:", segunda_variable)
    funcion3()


def funcion1():
    primera_variable = "valor en funcion1"
    print("funcion1 -> primera_variable:", primera_variable)
    funcion2()


def inicio():
    variable_inicial = "valor en inicio"
    print("inicio -> variable_inicial:", variable_inicial)
    funcion1()


if __name__ == "__main__":
    inicio()
