"""
Ejercicio 2 - Patrón: SINGLETON
================================
Clase para el cálculo de impuestos, compartida por todas las clases
que necesiten realizarlo. Garantiza una única instancia global.

Impuestos calculados sobre la base imponible:
  - IVA                    : 21 %
  - IIBB (Ingresos Brutos) :  5 %
  - Contribuciones munic.  :  1,2 %
  Total adicional          : 27,2 %

Roles del patrón:
  # Singleton: CalculadorImpuestos
    - _instancia   : única instancia de clase
    - __new__()    : punto de acceso global / control de creación
    - calcular()   : método de negocio principal
    - detalle()    : desglosa cada impuesto por separado
"""

TASA_IVA   = 0.21
TASA_IIBB  = 0.05
TASA_MUNIC = 0.012


class CalculadorImpuestos:
    # Singleton: única instancia almacenada como atributo de clase
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            print("[Singleton] Nueva instancia de CalculadorImpuestos creada.")
        else:
            print("[Singleton] Reutilizando instancia existente de CalculadorImpuestos.")
        return cls._instancia

    # ── Métodos de negocio ──────────────────────────────────────────

    def iva(self, base: float) -> float:
        return round(base * TASA_IVA, 2)

    def iibb(self, base: float) -> float:
        return round(base * TASA_IIBB, 2)

    def contribuciones_municipales(self, base: float) -> float:
        return round(base * TASA_MUNIC, 2)

    def calcular(self, base: float) -> float:
        """Retorna el total de impuestos sobre la base imponible."""
        total = self.iva(base) + self.iibb(base) + self.contribuciones_municipales(base)
        return round(total, 2)

    def detalle(self, base: float) -> dict:
        """Retorna un diccionario con el desglose de cada impuesto."""
        return {
            "base_imponible"            : round(base, 2),
            "IVA (21%)"                 : self.iva(base),
            "IIBB (5%)"                 : self.iibb(base),
            "Contribuciones munic (1.2%)": self.contribuciones_municipales(base),
            "TOTAL impuestos"           : self.calcular(base),
        }


# ──────────────────────────────────────────────
# Clientes que usan el calculador de impuestos
# ──────────────────────────────────────────────
class SistemaFacturacion:
    def __init__(self):
        self.impuestos = CalculadorImpuestos()   # obtiene el Singleton

    def procesar_venta(self, base: float):
        det = self.impuestos.detalle(base)
        print("\n[SistemaFacturacion] Desglose de impuestos:")
        for k, v in det.items():
            print(f"  {k:35s}: $ {v:>10.2f}")


class SistemaCompras:
    def __init__(self):
        self.impuestos = CalculadorImpuestos()   # misma instancia Singleton

    def calcular_costo_total(self, base: float):
        impuesto = self.impuestos.calcular(base)
        total    = round(base + impuesto, 2)
        print(f"\n[SistemaCompras] Base: ${base:.2f} | "
              f"Impuestos: ${impuesto:.2f} | Total: ${total:.2f}")


if __name__ == "__main__":
    print("=== Ejercicio 2: Singleton – Cálculo de Impuestos ===\n")

    facturacion = SistemaFacturacion()
    facturacion.procesar_venta(1000.0)

    compras = SistemaCompras()
    compras.calcular_costo_total(500.0)

    print(f"\n¿Misma instancia en ambos sistemas? "
          f"{facturacion.impuestos is compras.impuestos}")
