"""
Ejercicio 3 - Patrón: FACTORY METHOD
======================================
Una comida rápida "Hamburguesa" puede ser entregada de tres formas:
  - En mostrador (Counter)
  - Retirada por el cliente (Takeaway)
  - Enviada por delivery (Delivery)

El Factory Method define en la clase base el método `crear_entrega()`
que las subclases concretas implementan para instanciar el tipo de
entrega apropiado, sin que el cliente conozca la clase concreta.

Roles del patrón:
  # ProductoAbstracto  : Entrega  (define la interfaz de entrega)
  # ProductoConcreto   : EntregaMostrador, EntregaTakeaway, EntregaDelivery
  # CreadorAbstracto   : Hamburguesa  (declara factory_method crear_entrega())
  # CreadorConcreto    : HamburguesaMostrador, HamburguesaTakeaway, HamburguesaDelivery
"""

from abc import ABC, abstractmethod


# ── Producto Abstracto ──────────────────────────────────────────────
class Entrega(ABC):
    """ProductoAbstracto: interfaz común para todos los modos de entrega."""

    @abstractmethod
    def entregar(self, item: str) -> None:
        """Imprime el método de entrega del ítem."""
        ...


# ── Productos Concretos ─────────────────────────────────────────────
class EntregaMostrador(Entrega):
    """ProductoConcreto: entrega en mostrador."""

    def entregar(self, item: str) -> None:
        print(f"[Mostrador]  '{item}' lista para retirar en el mostrador. ¡Número de turno llamado!")


class EntregaTakeaway(Entrega):
    """ProductoConcreto: el cliente retira su pedido."""

    def entregar(self, item: str) -> None:
        print(f"[Takeaway]   '{item}' lista para que el cliente la retire en la ventanilla.")


class EntregaDelivery(Entrega):
    """ProductoConcreto: envío a domicilio."""

    def entregar(self, item: str) -> None:
        print(f"[Delivery]   '{item}' en camino hacia el domicilio del cliente. 🛵")


# ── Creador Abstracto ───────────────────────────────────────────────
class Hamburguesa(ABC):
    """
    CreadorAbstracto: conoce el ítem que fabrica y delega el modo
    de entrega al Factory Method crear_entrega().
    """

    def __init__(self, nombre: str = "Hamburguesa clásica"):
        self.nombre = nombre

    # Factory Method – las subclases lo sobreescriben
    @abstractmethod
    def crear_entrega(self) -> Entrega:
        """Factory Method: retorna el objeto Entrega adecuado."""
        ...

    def servir(self) -> None:
        """Operación plantilla que usa el Factory Method."""
        print(f"\nPreparando: {self.nombre}")
        entrega = self.crear_entrega()   # <── Factory Method
        entrega.entregar(self.nombre)


# ── Creadores Concretos ─────────────────────────────────────────────
class HamburguesaMostrador(Hamburguesa):
    """CreadorConcreto: instancia EntregaMostrador."""

    def crear_entrega(self) -> Entrega:
        return EntregaMostrador()


class HamburguesaTakeaway(Hamburguesa):
    """CreadorConcreto: instancia EntregaTakeaway."""

    def crear_entrega(self) -> Entrega:
        return EntregaTakeaway()


class HamburguesaDelivery(Hamburguesa):
    """CreadorConcreto: instancia EntregaDelivery."""

    def crear_entrega(self) -> Entrega:
        return EntregaDelivery()


# ──────────────────────────────────────────────
# Demostración
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Ejercicio 3: Factory Method – Hamburguesa ===")

    pedidos = [
        HamburguesaMostrador("Hamburguesa BBQ"),
        HamburguesaTakeaway("Hamburguesa Doble"),
        HamburguesaDelivery("Hamburguesa Vegana"),
    ]

    for pedido in pedidos:
        pedido.servir()
