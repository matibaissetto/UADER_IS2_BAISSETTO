"""
Ejercicio 5 - Patrón: BUILDER
================================
Extensión del ejemplo de vehículos visto en clase, adaptado para
construir aviones. Un avión tiene:
  - 1 body
  - 2 turbinas
  - 2 alas
  - 1 tren de aterrizaje

El Director orquesta los pasos de construcción a través de la
interfaz del Builder. El ConcreteBuilder ensambla cada parte y
al final entrega el Producto terminado.

Roles del patrón:
  # Producto         : Avion
  # BuilderAbstracto : AvionBuilder  (interfaz con los pasos de construcción)
  # BuilderConcreto  : AvionComercialBuilder  (implementación concreta)
  # Director         : DirectorAvion  (orquesta los pasos del Builder)
"""

from abc import ABC, abstractmethod


# ── Producto ────────────────────────────────────────────────────────
class Avion:
    """Producto: representa el avión ensamblado."""

    def __init__(self):
        self.body             = None
        self.turbinas         = []
        self.alas             = []
        self.tren_aterrizaje  = None

    def __str__(self) -> str:
        return (
            f"\n{'═' * 45}\n"
            f"  AVIÓN ENSAMBLADO\n"
            f"{'═' * 45}\n"
            f"  Body            : {self.body}\n"
            f"  Turbinas        : {', '.join(self.turbinas)}\n"
            f"  Alas            : {', '.join(self.alas)}\n"
            f"  Tren aterrizaje : {self.tren_aterrizaje}\n"
            f"{'═' * 45}"
        )


# ── Builder Abstracto ───────────────────────────────────────────────
class AvionBuilder(ABC):
    """BuilderAbstracto: declara los pasos de construcción."""

    @abstractmethod
    def construir_body(self) -> None: ...

    @abstractmethod
    def construir_turbinas(self) -> None: ...

    @abstractmethod
    def construir_alas(self) -> None: ...

    @abstractmethod
    def construir_tren_aterrizaje(self) -> None: ...

    @abstractmethod
    def get_avion(self) -> Avion: ...


# ── Builder Concreto ────────────────────────────────────────────────
class AvionComercialBuilder(AvionBuilder):
    """BuilderConcreto: ensambla un avión comercial paso a paso."""

    def __init__(self):
        self._avion = Avion()

    def construir_body(self) -> None:
        # Paso 1: body del avión
        self._avion.body = "Fuselaje de aluminio (wide-body)"
        print("  [Builder] Body construido.")

    def construir_turbinas(self) -> None:
        # Paso 2: 2 turbinas
        for i in range(1, 3):
            self._avion.turbinas.append(f"Turbina #{i} (CFM56)")
            print(f"  [Builder] Turbina #{i} instalada.")

    def construir_alas(self) -> None:
        # Paso 3: 2 alas
        for lado in ("Ala izquierda", "Ala derecha"):
            self._avion.alas.append(f"{lado} (winglet integrado)")
            print(f"  [Builder] {lado} ensamblada.")

    def construir_tren_aterrizaje(self) -> None:
        # Paso 4: tren de aterrizaje
        self._avion.tren_aterrizaje = "Tren triciclo retráctil"
        print("  [Builder] Tren de aterrizaje montado.")

    def get_avion(self) -> Avion:
        """Retorna el producto final y reinicia el builder."""
        avion          = self._avion
        self._avion    = Avion()   # listo para construir el próximo
        return avion


class AvionCargaBuilder(AvionBuilder):
    """BuilderConcreto alternativo: ensambla un avión de carga."""

    def __init__(self):
        self._avion = Avion()

    def construir_body(self) -> None:
        self._avion.body = "Fuselaje reforzado para carga pesada"
        print("  [Builder Carga] Body construido.")

    def construir_turbinas(self) -> None:
        for i in range(1, 3):
            self._avion.turbinas.append(f"Turbina #{i} (GE90 – alta potencia)")
            print(f"  [Builder Carga] Turbina #{i} instalada.")

    def construir_alas(self) -> None:
        for lado in ("Ala izquierda reforzada", "Ala derecha reforzada"):
            self._avion.alas.append(lado)
            print(f"  [Builder Carga] {lado} ensamblada.")

    def construir_tren_aterrizaje(self) -> None:
        self._avion.tren_aterrizaje = "Tren boggie de 16 ruedas"
        print("  [Builder Carga] Tren de aterrizaje montado.")

    def get_avion(self) -> Avion:
        avion       = self._avion
        self._avion = Avion()
        return avion


# ── Director ────────────────────────────────────────────────────────
class DirectorAvion:
    """
    Director: conoce el orden correcto de los pasos de construcción
    y los delega al Builder. No depende del tipo concreto de Builder.
    """

    def __init__(self, builder: AvionBuilder):
        self._builder = builder

    def cambiar_builder(self, builder: AvionBuilder) -> None:
        self._builder = builder

    def construir_avion_completo(self) -> None:
        """Orquesta la construcción completa paso a paso."""
        print("\n[Director] Iniciando construcción del avión...")
        self._builder.construir_body()
        self._builder.construir_turbinas()
        self._builder.construir_alas()
        self._builder.construir_tren_aterrizaje()
        print("[Director] Construcción finalizada.")


# ──────────────────────────────────────────────
# Demostración
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Ejercicio 5: Builder – Construcción de Aviones ===")

    # --- Avión comercial ---
    builder_comercial = AvionComercialBuilder()
    director = DirectorAvion(builder_comercial)
    director.construir_avion_completo()
    avion1 = builder_comercial.get_avion()
    print(avion1)

    # --- Avión de carga (mismo Director, Builder diferente) ---
    builder_carga = AvionCargaBuilder()
    director.cambiar_builder(builder_carga)
    director.construir_avion_completo()
    avion2 = builder_carga.get_avion()
    print(avion2)
