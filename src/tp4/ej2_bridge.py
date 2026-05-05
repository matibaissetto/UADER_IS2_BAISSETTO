"""
TP4 - Ejercicio 2: Patrón BRIDGE
==================================
Abstracción: Lamina (genérica, no sabe nada del tren)
Implementaciones: TrenLaminador5m, TrenLaminador10m

El Bridge separa QUÉ es la lámina de CÓMO se produce.
Podés cambiar el tren sin tocar la clase Lamina.
"""

from abc import ABC, abstractmethod


# ─── IMPLEMENTACIÓN (lado derecho del bridge) ─────────────────
class TrenLaminador(ABC):
    """Interfaz común para todos los trenes laminadores."""

    @abstractmethod
    def producir(self, espesor: float, ancho: float) -> None:
        pass


class TrenLaminador5m(TrenLaminador):
    """Tren que produce planchas de 5 metros de largo."""

    def producir(self, espesor: float, ancho: float) -> None:
        print(f"  [Tren 5m] Produciendo plancha: {espesor}\" espesor | {ancho}m ancho | 5m largo")


class TrenLaminador10m(TrenLaminador):
    """Tren que produce planchas de 10 metros de largo."""

    def producir(self, espesor: float, ancho: float) -> None:
        print(f"  [Tren 10m] Produciendo plancha: {espesor}\" espesor | {ancho}m ancho | 10m largo")


# ─── ABSTRACCIÓN (lado izquierdo del bridge) ──────────────────
class Lamina:
    """
    Representa una lámina de acero genérica.
    Recibe el tren laminador a usar (Bridge: composición sobre herencia).
    """

    def __init__(self, espesor: float, ancho: float, tren: TrenLaminador):
        self.espesor = espesor   # en pulgadas
        self.ancho   = ancho     # en metros
        self._tren   = tren      # implementación inyectada

    def cambiar_tren(self, tren: TrenLaminador) -> None:
        """Permite cambiar el tren en tiempo de ejecución."""
        print(f"  [Lamina] Cambiando tren laminador...")
        self._tren = tren

    def producir(self) -> None:
        """Delega la producción al tren asignado."""
        print(f"\n[Lamina] Lámina de acero {self.espesor}\" x {self.ancho}m → enviando a producir:")
        self._tren.producir(self.espesor, self.ancho)


# ─── CLIENTE ──────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  TP4 - Ejercicio 2: Patrón Bridge (Laminadora)")
    print("=" * 55)

    tren5  = TrenLaminador5m()
    tren10 = TrenLaminador10m()

    # Lámina estándar del enunciado: 0.5" de espesor, 1.5m de ancho
    lamina = Lamina(espesor=0.5, ancho=1.5, tren=tren5)
    lamina.producir()

    # Cambio de tren en tiempo de ejecución (sin tocar la clase Lamina)
    lamina.cambiar_tren(tren10)
    lamina.producir()

    # Una segunda lámina con diferentes medidas, directo al tren de 10m
    lamina2 = Lamina(espesor=0.5, ancho=1.5, tren=tren10)
    lamina2.producir()