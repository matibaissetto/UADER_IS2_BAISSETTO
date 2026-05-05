"""
TP4 - Ejercicio 3: Patrón COMPOSITE
=====================================
Producto principal → 3 subconjuntos → 4 piezas cada uno.
Se agrega/remueve un subconjunto opcional con 4 piezas más.

Con Composite, el cliente trata igual a piezas individuales
(Leaf) que a grupos de piezas (Composite). Ambos implementan
la misma interfaz: mostrar().
"""

from abc import ABC, abstractmethod


# ─── COMPONENTE (interfaz común) ──────────────────────────────
class Componente(ABC):

    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def mostrar(self, nivel: int = 0) -> None:
        pass


# ─── LEAF: pieza individual (no tiene hijos) ──────────────────
class Pieza(Componente):

    def mostrar(self, nivel: int = 0) -> None:
        print("  " * nivel + f" {self.nombre}")


# ─── COMPOSITE: subconjunto o producto (tiene hijos) ──────────
class Conjunto(Componente):

    def __init__(self, nombre: str):
        super().__init__(nombre)
        self._hijos: list[Componente] = []

    def agregar(self, componente: Componente) -> None:
        self._hijos.append(componente)
        print(f"  [+] '{componente.nombre}' agregado a '{self.nombre}'")

    def remover(self, componente: Componente) -> None:
        self._hijos.remove(componente)
        print(f"  [-] '{componente.nombre}' removido de '{self.nombre}'")

    def mostrar(self, nivel: int = 0) -> None:
        print("  " * nivel + f" {self.nombre}")
        for hijo in self._hijos:
            hijo.mostrar(nivel + 1)


# ─── CLIENTE ──────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  TP4 - Ejercicio 3: Patrón Composite (Ensamblado)")
    print("=" * 55)

    # Producto principal
    producto = Conjunto("Producto Principal")

    # Tres subconjuntos con 4 piezas cada uno
    for idx in range(1, 4):
        sub = Conjunto(f"Subconjunto {idx}")
        for j in range(1, 5):
            sub.agregar(Pieza(f"Pieza {idx}.{j}"))
        producto.agregar(sub)

    print("\n--- Estructura inicial ---")
    producto.mostrar()

    # Agregar subconjunto opcional
    print("\n--- Agregando subconjunto opcional ---")
    opcional = Conjunto("Subconjunto Opcional (4)")
    for j in range(1, 5):
        opcional.agregar(Pieza(f"Pieza 4.{j}"))
    producto.agregar(opcional)

    print("\n--- Estructura con subconjunto opcional ---")
    producto.mostrar()

    # Remover el subconjunto opcional
    print("\n--- Removiendo subconjunto opcional ---")
    producto.remover(opcional)

    print("\n--- Estructura final (sin opcional) ---")
    producto.mostrar()