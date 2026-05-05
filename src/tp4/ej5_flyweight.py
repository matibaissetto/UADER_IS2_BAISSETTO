"""
TP4 - Ejercicio 5: Patrón FLYWEIGHT
=====================================
Situación imaginada: un videojuego con miles de enemigos en pantalla.
Cada tipo de enemigo (Goblin, Orco, Dragon) tiene datos compartidos
pesados: sprite, color, sonido. Son siempre los mismos para todos los
enemigos del mismo tipo. No tiene sentido crear un objeto distinto con
esos datos para CADA enemigo instanciado.

FLYWEIGHT: los datos compartidos (intrínsecos) se guardan en UN solo
objeto por tipo. Los datos únicos de cada instancia (posición, vida)
son extrínsecos y se pasan en cada operación.

Sin Flyweight: 1000 Goblins = 1000 objetos con sprite+color+sonido c/u.
Con Flyweight: 1000 Goblins = 1 FlyweightEnemigo + 1000 contextos pequeños.
"""


# ─── FLYWEIGHT: datos compartidos (intrínsecos) ───────────────
class FlyweightEnemigo:
    """
    Contiene solo los datos que son IGUALES para todos los enemigos
    del mismo tipo: sprite, color, sonido de ataque.
    Este objeto se comparte — nunca se duplica.
    """

    def __init__(self, tipo: str, sprite: str, color: str, sonido: str):
        self.tipo    = tipo
        self.sprite  = sprite   # datos "pesados" compartidos
        self.color   = color
        self.sonido  = sonido
        print(f"  [Flyweight] Creando tipo '{tipo}' (sprite='{sprite}')")

    def renderizar(self, x: float, y: float, vida: int) -> None:
        """
        Recibe los datos extrínsecos (únicos por instancia)
        y los combina con los intrínsecos para renderizar.
        """
        print(f"  Renderizando {self.color} {self.tipo} | "
            f"pos=({x:.0f},{y:.0f}) | vida={vida} | "
            f"sprite={self.sprite} | sfx={self.sonido}")


# ─── FLYWEIGHT FACTORY: caché de flyweights ───────────────────
class EnemigosFactory:
    """
    Devuelve el flyweight del tipo solicitado.
    Si ya existe en caché, lo reutiliza. Si no, lo crea.
    """
    _cache: dict[str, FlyweightEnemigo] = {}

    @classmethod
    def get(cls, tipo: str, sprite: str, color: str, sonido: str) -> FlyweightEnemigo:
        if tipo not in cls._cache:
            cls._cache[tipo] = FlyweightEnemigo(tipo, sprite, color, sonido)
        else:
            print(f"  [Factory] Reutilizando flyweight '{tipo}' (no se duplica)")
        return cls._cache[tipo]

    @classmethod
    def cantidad_tipos(cls) -> int:
        return len(cls._cache)


# ─── CONTEXTO: datos únicos por instancia (extrínsecos) ───────
class Enemigo:
    """
    Representa UNA instancia de enemigo en el mapa.
    Solo guarda su posición y vida (datos livianos).
    El resto lo obtiene del flyweight compartido.
    """

    def __init__(self, tipo: str, sprite: str, color: str,
                sonido: str, x: float, y: float, vida: int):
        self._flyweight = EnemigosFactory.get(tipo, sprite, color, sonido)
        self.x    = x
        self.y    = y
        self.vida = vida

    def renderizar(self) -> None:
        self._flyweight.renderizar(self.x, self.y, self.vida)


# ─── CLIENTE ──────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  TP4 - Ejercicio 5: Patrón Flyweight (Videojuego)")
    print("=" * 55)

    print("\n--- Instanciando 6 enemigos (3 tipos) ---")
    enemigos = [
        Enemigo("Goblin", "goblin.png", "Verde",  "¡Gruñido!",  10, 20, 30),
        Enemigo("Goblin", "goblin.png", "Verde",  "¡Gruñido!",  55, 80, 18),
        Enemigo("Goblin", "goblin.png", "Verde",  "¡Gruñido!",  33, 45, 25),
        Enemigo("Orco",   "orco.png",   "Gris",   "¡Rugido!",   70, 15, 80),
        Enemigo("Orco",   "orco.png",   "Gris",   "¡Rugido!",   90, 50, 60),
        Enemigo("Dragon", "dragon.png", "Rojo",   "¡Fuego!",    5,  5,  200),
    ]

    print(f"\n--- Renderizando los {len(enemigos)} enemigos ---")
    for e in enemigos:
        e.renderizar()

    print(f"\n--- Resultado Flyweight ---")
    print(f"  Enemigos instanciados : {len(enemigos)}")
    print(f"  Flyweights en memoria : {EnemigosFactory.cantidad_tipos()}  ← solo 3 objetos compartidos")
    print(f"  (En lugar de {len(enemigos)} objetos con sprite+color+sonido cada uno)")
    