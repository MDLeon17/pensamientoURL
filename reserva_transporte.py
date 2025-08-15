from abc import ABC, abstractmethod


class Transporte(ABC):
    @abstractmethod
    def reservar(self, asientos: int) -> None:
        """Reserva un número de asientos."""
        pass

    @abstractmethod
    def cancelar(self, asientos: int) -> None:
        """Cancela un número de asientos."""
        pass


class Avion(Transporte):
    def __init__(self, total_asientos: int = 100) -> None:
        # 1 representa asiento disponible, 0 reservado
        self.asientos = [1] * total_asientos

    def reservar(self, asientos: int) -> None:
        reservados = 0
        for i, estado in enumerate(self.asientos):
            if estado == 1:
                self.asientos[i] = 0
                reservados += 1
                if reservados == asientos:
                    break
        if reservados < asientos:
            print("Avión: no hay suficientes asientos disponibles")
        else:
            print(f"Avión reservó {reservados} asientos")
        print(f"Estado de asientos: {self.asientos}")

    def cancelar(self, asientos: int) -> None:
        cancelados = 0
        for i, estado in enumerate(self.asientos):
            if estado == 0:
                self.asientos[i] = 1
                cancelados += 1
                if cancelados == asientos:
                    break
        print(f"Avión canceló {cancelados} asientos")
        print(f"Estado de asientos: {self.asientos}")


class Autobus(Transporte):
    def __init__(self, total_asientos: int = 40) -> None:
        self.asientos = [1] * total_asientos

    def reservar(self, asientos: int) -> None:
        disponibles = self.asientos.count(1)
        if asientos > disponibles:
            print("Autobús: no hay suficientes asientos disponibles")
            return
        reservados = 0
        for i, estado in enumerate(self.asientos):
            if estado == 1:
                self.asientos[i] = 0
                reservados += 1
                if reservados == asientos:
                    break
        print(f"Autobús reservó {reservados} asientos")
        print(f"Estado de asientos: {self.asientos}")

    def cancelar(self, asientos: int) -> None:
        cancelados = 0
        for i, estado in enumerate(self.asientos):
            if estado == 0:
                self.asientos[i] = 1
                cancelados += 1
                if cancelados == asientos:
                    break
        print(f"Autobús canceló {cancelados} asientos")
        print(f"Estado de asientos: {self.asientos}")


class Tren(Transporte):
    def __init__(self, vagones: int = 5, asientos_por_vagon: int = 20) -> None:
        self.vagones = {
            f"Vagón {i+1}": [1] * asientos_por_vagon for i in range(vagones)
        }

    def reservar(self, asientos: int) -> None:
        reservados = 0
        for vagon, lista in self.vagones.items():
            for i, estado in enumerate(lista):
                if estado == 1:
                    lista[i] = 0
                    reservados += 1
                    if reservados == asientos:
                        break
            if reservados == asientos:
                break
        if reservados < asientos:
            print("Tren: no hay suficientes asientos disponibles")
        else:
            print(f"Tren reservó {reservados} asientos")
        print(f"Estado de vagones: {self.vagones}")

    def cancelar(self, asientos: int) -> None:
        cancelados = 0
        for vagon, lista in self.vagones.items():
            for i, estado in enumerate(lista):
                if estado == 0:
                    lista[i] = 1
                    cancelados += 1
                    if cancelados == asientos:
                        break
            if cancelados == asientos:
                break
        print(f"Tren canceló {cancelados} asientos")
        print(f"Estado de vagones: {self.vagones}")


def hacer_reserva(transporte: Transporte, asientos: int) -> None:
    transporte.reservar(asientos)


def cancelar_reserva(transporte: Transporte, asientos: int) -> None:
    transporte.cancelar(asientos)


if __name__ == "__main__":
    medios: list[Transporte] = [Avion(), Autobus(), Tren()]
    for medio in medios:
        hacer_reserva(medio, 3)
        cancelar_reserva(medio, 1)
