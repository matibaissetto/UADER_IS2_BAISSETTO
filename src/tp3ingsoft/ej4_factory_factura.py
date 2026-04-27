"""
Ejercicio 4 - Patrón: FACTORY METHOD
======================================
Clase "Factura" que, según la condición impositiva del cliente,
genera facturas distintas:
  - IVA Responsable   → Factura A
  - IVA No Inscripto  → Factura B
  - IVA Exento        → Factura C  (o "E" en algunas jurisdicciones)

El Factory Method `crear_factura()` en la clase base encapsula
la decisión de qué tipo concreto de factura instanciar.

Roles del patrón:
  # ProductoAbstracto  : FacturaBase
  # ProductoConcreto   : FacturaA, FacturaB, FacturaC
  # CreadorAbstracto   : EmisorFactura  (Factory Method: crear_factura())
  # CreadorConcreto    : EmisorFacturaResponsable, EmisorFacturaNoInscripto,
                         EmisorFacturaExento
"""

from abc import ABC, abstractmethod


# ── Producto Abstracto ──────────────────────────────────────────────
class FacturaBase(ABC):
    """ProductoAbstracto: interfaz común de todas las facturas."""

    def __init__(self, importe: float):
        self.importe = importe

    @abstractmethod
    def tipo(self) -> str:
        """Retorna la letra/tipo de factura."""
        ...

    @abstractmethod
    def condicion_cliente(self) -> str:
        """Descripción de la condición impositiva."""
        ...

    def imprimir(self) -> None:
        linea = "─" * 40
        print(f"\n{linea}")
        print(f"  FACTURA TIPO {self.tipo()}")
        print(f"{linea}")
        print(f"  Condición IVA : {self.condicion_cliente()}")
        print(f"  Importe Total : $ {self.importe:>10.2f}")
        print(f"{linea}")


# ── Productos Concretos ─────────────────────────────────────────────
class FacturaA(FacturaBase):
    """ProductoConcreto: para clientes IVA Responsable."""

    def tipo(self) -> str:
        return "A"

    def condicion_cliente(self) -> str:
        return "IVA Responsable Inscripto"


class FacturaB(FacturaBase):
    """ProductoConcreto: para clientes IVA No Inscripto."""

    def tipo(self) -> str:
        return "B"

    def condicion_cliente(self) -> str:
        return "IVA No Inscripto / Consumidor Final"


class FacturaC(FacturaBase):
    """ProductoConcreto: para clientes IVA Exento."""

    def tipo(self) -> str:
        return "C"

    def condicion_cliente(self) -> str:
        return "IVA Exento"


# ── Creador Abstracto ───────────────────────────────────────────────
class EmisorFactura(ABC):
    """
    CreadorAbstracto: conoce el importe y delega la creación
    del tipo concreto de factura al Factory Method.
    """

    def __init__(self, importe: float):
        self.importe = importe

    # Factory Method
    @abstractmethod
    def crear_factura(self) -> FacturaBase:
        """Factory Method: instancia el tipo concreto de factura."""
        ...

    def emitir(self) -> None:
        """Operación plantilla que usa el Factory Method."""
        factura = self.crear_factura()   # <── Factory Method
        factura.imprimir()


# ── Creadores Concretos ─────────────────────────────────────────────
class EmisorFacturaResponsable(EmisorFactura):
    """CreadorConcreto: emite Factura A para IVA Responsable."""

    def crear_factura(self) -> FacturaBase:
        return FacturaA(self.importe)


class EmisorFacturaNoInscripto(EmisorFactura):
    """CreadorConcreto: emite Factura B para IVA No Inscripto."""

    def crear_factura(self) -> FacturaBase:
        return FacturaB(self.importe)


class EmisorFacturaExento(EmisorFactura):
    """CreadorConcreto: emite Factura C para IVA Exento."""

    def crear_factura(self) -> FacturaBase:
        return FacturaC(self.importe)


# ──────────────────────────────────────────────
# Función auxiliar: elige el emisor según condición
# ──────────────────────────────────────────────
def obtener_emisor(condicion: str, importe: float) -> EmisorFactura:
    """
    Factory simple que mapea la condición impositiva
    al EmisorFactura correcto.
    """
    mapa = {
        "responsable"  : EmisorFacturaResponsable,
        "no_inscripto" : EmisorFacturaNoInscripto,
        "exento"       : EmisorFacturaExento,
    }
    clase = mapa.get(condicion.lower())
    if clase is None:
        raise ValueError(f"Condición desconocida: '{condicion}'. "
                         f"Use: {list(mapa.keys())}")
    return clase(importe)


# ──────────────────────────────────────────────
# Demostración
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Ejercicio 4: Factory Method – Factura ===")

    ventas = [
        ("responsable",   15_000.00),
        ("no_inscripto",   8_500.50),
        ("exento",         3_200.00),
    ]

    for condicion, importe in ventas:
        emisor = obtener_emisor(condicion, importe)
        emisor.emitir()
