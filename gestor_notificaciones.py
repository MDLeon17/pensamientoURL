from abc import ABC, abstractmethod
from typing import Iterable

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str) -> None:
        pass

class Email(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"Email enviado: {mensaje}")

class SMS(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"SMS enviado: {mensaje}")

class PushApp(Notificacion):
    def enviar(self, mensaje: str) -> None:
        print(f"PushApp enviado: {mensaje}")

def enviar_a_todos(canales: Iterable[Notificacion], mensaje: str) -> None:
    for canal in canales:
        canal.enviar(mensaje)

if __name__ == "__main__":
    canales = [Email(), SMS(), PushApp()]
    enviar_a_todos(canales, "Hola desde el gestor de notificaciones")
