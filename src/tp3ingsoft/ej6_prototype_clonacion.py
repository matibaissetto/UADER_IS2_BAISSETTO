"""
Ejercicio 6 - Patrón: PROTOTYPE
=================================
Demuestra que una clase generada a partir de un prototipo
puede a su vez generar copias de sí misma (clonación anidada).

Cada clase implementa el método clone() que retorna una copia
profunda (deep copy) de la instancia. Esto garantiza que atributos
compuestos no sean compartidos entre el original y el clon.

Roles del patrón:
  # ClasePrototipo (interfaz): define clone()
  # ClaseA        : implementa clone(); es el prototipo original
  # ClaseB        : clonada a partir de ClaseA; también implementa clone()
                    verificando que una clase derivada del prototipo
                    puede igualmente clonarse a sí misma.
"""

import copy
from abc import ABC, abstractmethod


# ── Prototipo Abstracto ─────────────────────────────────────────────
class ClasePrototipo(ABC):
    """ClasePrototipo: interfaz que obliga a implementar clone()."""

    @abstractmethod
    def clone(self) -> "ClasePrototipo":
        """Retorna una copia profunda de la instancia."""
        ...

    @abstractmethod
    def __str__(self) -> str: ...


# ── Clase A (Prototipo concreto original) ───────────────────────────
class ClaseA(ClasePrototipo):
    """
    ProductoConcreto A: prototipo original.
    Tiene atributos simples y compuestos (lista) para demostrar
    que el clon es independiente del original.
    """

    def __init__(self, nombre: str, valores: list):
        self.nombre  = nombre
        self.valores = valores          # atributo compuesto

    def metodo_a(self) -> str:
        return f"[ClaseA.metodo_a] nombre={self.nombre}, valores={self.valores}"

    def metodo_b(self, x: int) -> None:
        self.valores.append(x)
        print(f"[ClaseA.metodo_b] Se agregó {x} → valores={self.valores}")

    def clone(self) -> "ClaseA":
        """Clona la instancia (deep copy para independencia total)."""
        clon = copy.deepcopy(self)
        print(f"[Prototype] ClaseA clonada → id original={id(self)}, id clon={id(clon)}")
        return clon

    def __str__(self) -> str:
        return f"ClaseA(nombre='{self.nombre}', valores={self.valores}) @ {id(self)}"


# ── Clase B (clonada a partir de ClaseA; también es prototipo) ──────
class ClaseB(ClasePrototipo):
    """
    ProductoConcreto B: instanciada a partir de los datos de un
    objeto ClaseA, pero es una clase propia con su propio clone().
    Verifica que una clase generada del prototipo también puede
    generar copias de sí misma.
    """

    def __init__(self, origen: ClaseA, descripcion: str):
        # Toma los datos del origen pero no los comparte (deep copy)
        self.nombre      = origen.nombre + "_B"
        self.valores     = copy.deepcopy(origen.valores)
        self.descripcion = descripcion

    def metodo_c(self) -> str:
        return (f"[ClaseB.metodo_c] nombre={self.nombre}, "
                f"descripcion={self.descripcion}, valores={self.valores}")

    def clone(self) -> "ClaseB":
        """ClaseB también puede clonarse a sí misma."""
        clon = copy.deepcopy(self)
        print(f"[Prototype] ClaseB clonada → id original={id(self)}, id clon={id(clon)}")
        return clon

    def __str__(self) -> str:
        return (f"ClaseB(nombre='{self.nombre}', descripcion='{self.descripcion}', "
                f"valores={self.valores}) @ {id(self)}")


# ──────────────────────────────────────────────
# Demostración
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Ejercicio 6: Prototype – Clonación anidada ===\n")

    # 1. Crear instancia original de ClaseA
    original_a = ClaseA("Prototipo_A", [1, 2, 3])
    print(f"Original A : {original_a}")
    print(original_a.metodo_a())

    # 2. Clonar ClaseA
    clon_a = original_a.clone()
    print(f"Clon A     : {clon_a}")

    # 3. Verificar independencia: modificar el clon no afecta al original
    print("\n--- Modificando el clon_a (agrego 99) ---")
    clon_a.metodo_b(99)
    print(f"Original A después: {original_a}")
    print(f"Clon A después    : {clon_a}")

    # 4. Crear ClaseB a partir del original_a → clase generada del prototipo
    print("\n--- Creando ClaseB a partir de original_a ---")
    objeto_b = ClaseB(original_a, "Clase derivada del prototipo A")
    print(f"Objeto B   : {objeto_b}")
    print(objeto_b.metodo_c())

    # 5. ClaseB también puede clonarse (verifica el enunciado)
    print("\n--- Clonando ClaseB ---")
    clon_b = objeto_b.clone()
    print(f"Clon B     : {clon_b}")

    # 6. Verificar que clon_b es independiente de objeto_b
    clon_b.descripcion = "DESCRIPCIÓN MODIFICADA"
    clon_b.valores.append(999)
    print(f"\nObjeto B después de modificar clon_b: {objeto_b}")
    print(f"Clon B modificado                    : {clon_b}")

    print("\n✔ Los clones son completamente independientes de sus originales.")
