"""
Ejercicio 1 - Patrón: SINGLETON
================================
Clase que calcula el factorial de un número entero,
garantizando que todas las clases que la invoquen
utilicen la misma instancia (una única instancia global).

Roles del patrón:
# Singleton: CalculadorFactorial
    - _instancia : atributo de clase que guarda la única instancia
    - __new__()  : controla la creación; retorna la instancia existente si ya fue creada
    - factorial(): método de negocio disponible desde la única instancia
"""


class CalculadorFactorial:
    # Singleton: atributo de clase que almacena la única instancia
    _instancia = None

    def __new__(cls):
        # Si no existe instancia, la crea; si ya existe, la reutiliza
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            print("[Singleton] Nueva instancia de CalculadorFactorial creada.")
        else:
            print("[Singleton] Reutilizando instancia existente.")
        return cls._instancia

    def factorial(self, n: int) -> int:
        """Retorna el factorial de n (n debe ser entero no negativo)."""
        if not isinstance(n, int) or n < 0:
            raise ValueError(f"El argumento debe ser un entero no negativo. Se recibió: {n}")
        if n == 0:
            return 1
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado


# ──────────────────────────────────────────────
# Demostración: dos clientes usan la misma instancia
# ──────────────────────────────────────────────
class ClienteA:
    def __init__(self):
        # Cada cliente obtiene la instancia a través del Singleton
        self.calc = CalculadorFactorial()

    def calcular(self, n):
        resultado = self.calc.factorial(n)
        print(f"[ClienteA] {n}! = {resultado}  (id instancia: {id(self.calc)})")


class ClienteB:
    def __init__(self):
        self.calc = CalculadorFactorial()

    def calcular(self, n):
        resultado = self.calc.factorial(n)
        print(f"[ClienteB] {n}! = {resultado}  (id instancia: {id(self.calc)})")


if __name__ == "__main__":
    print("=== Ejercicio 1: Singleton – Factorial ===\n")

    a = ClienteA()
    a.calcular(5)

    b = ClienteB()
    b.calcular(7)

    # Verificación explícita: ambos clientes comparten la misma instancia
    print(f"\n¿ClienteA y ClienteB usan la misma instancia? "
          f"{a.calc is b.calc}")
