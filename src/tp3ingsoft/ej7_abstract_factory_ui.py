"""
Ejercicio 7 - Patrón: ABSTRACT FACTORY
=========================================
Situación imaginada: una aplicación de escritorio que debe renderizar
su interfaz gráfica (UI) de manera diferente según el sistema operativo
en el que se ejecuta (Windows, macOS, Linux/GTK).

El Abstract Factory garantiza que todos los widgets creados sean
consistentes entre sí (misma familia de estilo), sin que el código
cliente conozca las clases concretas de cada plataforma.

Roles del patrón:
  # FábricaAbstracta : UIFactory (crea familias de widgets compatibles)
  # FábricaConcreta  : WindowsUIFactory, MacOSUIFactory, LinuxUIFactory
  # ProductoA Abst.  : Boton       (interfaz de botón)
  # ProductoA Conc.  : WindowsBoton, MacOSBoton, LinuxBoton
  # ProductoB Abst.  : CampoTexto  (interfaz de campo de texto)
  # ProductoB Conc.  : WindowsCampoTexto, MacOSCampoTexto, LinuxCampoTexto
  # ProductoC Abst.  : Ventana     (interfaz de ventana / frame)
  # ProductoC Conc.  : WindowsVentana, MacOSVentana, LinuxVentana
  # Cliente          : Aplicacion  (usa la fábrica sin conocer la plataforma)
"""

from abc import ABC, abstractmethod
import platform


# ══════════════════════════════════════════════
# PRODUCTOS ABSTRACTOS
# ══════════════════════════════════════════════

class Boton(ABC):
    """ProductoAbstracto A: interfaz de botón."""
    @abstractmethod
    def render(self) -> str: ...
    @abstractmethod
    def on_click(self) -> str: ...


class CampoTexto(ABC):
    """ProductoAbstracto B: interfaz de campo de texto."""
    @abstractmethod
    def render(self) -> str: ...
    @abstractmethod
    def get_valor(self) -> str: ...


class Ventana(ABC):
    """ProductoAbstracto C: interfaz de ventana."""
    @abstractmethod
    def mostrar(self, titulo: str) -> str: ...


# ══════════════════════════════════════════════
# FAMILIA WINDOWS
# ══════════════════════════════════════════════

class WindowsBoton(Boton):
    """ProductoConcreto A – Windows."""
    def render(self)    -> str: return "[Windows] 🪟 Botón con borde biselado y sombra."
    def on_click(self)  -> str: return "[Windows] Click! – Sonido 'ding' del sistema."

class WindowsCampoTexto(CampoTexto):
    """ProductoConcreto B – Windows."""
    def render(self)     -> str: return "[Windows] 🪟 CampoTexto con borde gris y fondo blanco."
    def get_valor(self)  -> str: return "valor_windows"

class WindowsVentana(Ventana):
    """ProductoConcreto C – Windows."""
    def mostrar(self, titulo: str) -> str:
        return f"[Windows] 🪟 Ventana '{titulo}' con barra azul y botones Min/Max/Close."


# ══════════════════════════════════════════════
# FAMILIA macOS
# ══════════════════════════════════════════════

class MacOSBoton(Boton):
    """ProductoConcreto A – macOS."""
    def render(self)    -> str: return "[macOS]    Botón redondeado con degradado."
    def on_click(self)  -> str: return "[macOS]   Click! – Animación de rebote."

class MacOSCampoTexto(CampoTexto):
    """ProductoConcreto B – macOS."""
    def render(self)     -> str: return "[macOS]    CampoTexto con borde azul al foco."
    def get_valor(self)  -> str: return "valor_macos"

class MacOSVentana(Ventana):
    """ProductoConcreto C – macOS."""
    def mostrar(self, titulo: str) -> str:
        return f"[macOS]    Ventana '{titulo}' con semáforo rojo/amarillo/verde."


# ══════════════════════════════════════════════
# FAMILIA LINUX / GTK
# ══════════════════════════════════════════════

class LinuxBoton(Boton):
    """ProductoConcreto A – Linux."""
    def render(self)    -> str: return "[Linux]    Botón GTK plano con borde fino."
    def on_click(self)  -> str: return "[Linux]   Click! – Sin sonido (depende del tema)."

class LinuxCampoTexto(CampoTexto):
    """ProductoConcreto B – Linux."""
    def render(self)     -> str: return "[Linux]    CampoTexto GTK con subrayado."
    def get_valor(self)  -> str: return "valor_linux"

class LinuxVentana(Ventana):
    """ProductoConcreto C – Linux."""
    def mostrar(self, titulo: str) -> str:
        return f"[Linux]    Ventana '{titulo}' con decoración del window manager activo."


# ══════════════════════════════════════════════
# FÁBRICA ABSTRACTA
# ══════════════════════════════════════════════

class UIFactory(ABC):
    """
    FábricaAbstracta: declara los métodos de creación para cada
    producto de la familia. Garantiza compatibilidad entre widgets.
    """
    @abstractmethod
    def crear_boton(self) -> Boton: ...

    @abstractmethod
    def crear_campo_texto(self) -> CampoTexto: ...

    @abstractmethod
    def crear_ventana(self) -> Ventana: ...


# ══════════════════════════════════════════════
# FÁBRICAS CONCRETAS
# ══════════════════════════════════════════════

class WindowsUIFactory(UIFactory):
    """FábricaConcreta: crea widgets de la familia Windows."""
    def crear_boton(self)       -> Boton:      return WindowsBoton()
    def crear_campo_texto(self) -> CampoTexto: return WindowsCampoTexto()
    def crear_ventana(self)     -> Ventana:    return WindowsVentana()


class MacOSUIFactory(UIFactory):
    """FábricaConcreta: crea widgets de la familia macOS."""
    def crear_boton(self)       -> Boton:      return MacOSBoton()
    def crear_campo_texto(self) -> CampoTexto: return MacOSCampoTexto()
    def crear_ventana(self)     -> Ventana:    return MacOSVentana()


class LinuxUIFactory(UIFactory):
    """FábricaConcreta: crea widgets de la familia Linux/GTK."""
    def crear_boton(self)       -> Boton:      return LinuxBoton()
    def crear_campo_texto(self) -> CampoTexto: return LinuxCampoTexto()
    def crear_ventana(self)     -> Ventana:    return LinuxVentana()


# ══════════════════════════════════════════════
# CLIENTE
# ══════════════════════════════════════════════

class Aplicacion:
    """
    Cliente: usa solo la interfaz UIFactory y los productos abstractos.
    No conoce ninguna clase concreta de plataforma.
    """

    def __init__(self, fabrica: UIFactory):
        # El cliente recibe la fábrica correcta desde el exterior
        self._boton       = fabrica.crear_boton()
        self._campo_texto = fabrica.crear_campo_texto()
        self._ventana     = fabrica.crear_ventana()

    def renderizar_ui(self, titulo: str = "Mi Aplicación") -> None:
        print(self._ventana.mostrar(titulo))
        print(self._boton.render())
        print(self._campo_texto.render())
        print(self._boton.on_click())


# ══════════════════════════════════════════════
# Selector automático de fábrica según SO
# ══════════════════════════════════════════════

def obtener_fabrica_por_sistema() -> UIFactory:
    """Selecciona la fábrica concreta en función del SO detectado."""
    so = platform.system()
    if so == "Windows":
        return WindowsUIFactory()
    elif so == "Darwin":   # macOS
        return MacOSUIFactory()
    else:                  # Linux y otros
        return LinuxUIFactory()


# ──────────────────────────────────────────────
# Demostración
# ──────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Ejercicio 7: Abstract Factory – UI Multiplataforma ===\n")

    # a) Detectar el SO y crear la fábrica correspondiente automáticamente
    fabrica_auto = obtener_fabrica_por_sistema()
    print(f"Sistema detectado: {platform.system()}")
    print(f"Fábrica elegida  : {type(fabrica_auto).__name__}\n")
    app_auto = Aplicacion(fabrica_auto)
    app_auto.renderizar_ui("Ventana Principal")

    # b) Forzar cada familia para demostrar compatibilidad
    print("\n" + "─" * 50)
    print("Simulación de las tres plataformas:\n")
    for nombre, fabrica in [
        ("Windows", WindowsUIFactory()),
        ("macOS",   MacOSUIFactory()),
        ("Linux",   LinuxUIFactory()),
    ]:
        print(f"── Plataforma: {nombre} ──")
        app = Aplicacion(fabrica)
        app.renderizar_ui(f"Demo {nombre}")
        print()
