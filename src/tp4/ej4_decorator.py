"""
TP4 - Ejercicio 4: Patrón DECORATOR
=====================================
Clase base Numero: guarda un valor y lo imprime.
Decoradores que se anidan (wrappers):
  - SumarDos    → valor + 2
  - MultiplicarDos → valor * 2
  - DividirTres → valor / 3

Se pueden combinar en cualquier orden. Cada decorator
llama al valor del interior y le aplica su operación.
"""

from abc import ABC, abstractmethod


# ─── COMPONENTE BASE ──────────────────────────────────────────
class NumeroBase(ABC):

    @abstractmethod
    def valor(self) -> float:
        pass

    def mostrar(self) -> None:
        print(f"  Resultado: {self.valor():.4f}")


# ─── CONCRETO ─────────────────────────────────────────────────
class Numero(NumeroBase):
    """Número concreto sin ningún decorador."""

    def __init__(self, n: float):
        self._n = n

    def valor(self) -> float:
        return self._n


# ─── DECORATOR BASE ───────────────────────────────────────────
class OperacionDecorator(NumeroBase, ABC):
    """Wrapper abstracto que envuelve cualquier NumeroBase."""

    def __init__(self, wrapped: NumeroBase):
        self._wrapped = wrapped   # el objeto interior


# ─── DECORADORES CONCRETOS ────────────────────────────────────
class SumarDos(OperacionDecorator):
    """Suma 2 al valor del interior."""

    def valor(self) -> float:
        return self._wrapped.valor() + 2


class MultiplicarDos(OperacionDecorator):
    """Multiplica por 2 el valor del interior."""

    def valor(self) -> float:
        return self._wrapped.valor() * 2


class DividirTres(OperacionDecorator):
    """Divide por 3 el valor del interior."""

    def valor(self) -> float:
        return self._wrapped.valor() / 3


# ─── CLIENTE ──────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  TP4 - Ejercicio 4: Patrón Decorator (Número)")
    print("=" * 55)

    n = 6.0
    print(f"\nNúmero base: {n}")

    # Sin decoradores
    base = Numero(n)
    print("\n[Sin decoradores]")
    base.mostrar()

    # + 2
    mas2 = SumarDos(Numero(n))
    print("\n[+ 2]")
    mas2.mostrar()

    # * 2
    por2 = MultiplicarDos(Numero(n))
    print("\n[* 2]")
    por2.mostrar()

    # / 3
    div3 = DividirTres(Numero(n))
    print("\n[/ 3]")
    div3.mostrar()

    # Anidados: ((n + 2) * 2) / 3
    combinado = DividirTres(MultiplicarDos(SumarDos(Numero(n))))
    print(f"\n[((n+2)*2)/3]  →  (({n}+2)*2)/3")
    combinado.mostrar()

    # Otro orden: (n * 2) + 2 luego / 3
    combinado2 = DividirTres(SumarDos(MultiplicarDos(Numero(n))))
    print(f"\n[((n*2)+2)/3]  →  (({n}*2)+2)/3")
    combinado2.mostrar()