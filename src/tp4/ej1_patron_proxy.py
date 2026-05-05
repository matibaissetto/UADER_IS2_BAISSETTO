"""
TP4 - Ejercicio 1: Patrón PROXY
================================
Clase Ping con control de IP (solo "192.x.x.x") y método libre sin control.
PingProxy intercepta: si la IP es "192.168.0.254" redirige a google.com,
en cualquier otro caso delega a Ping.execute() normalmente.
"""

import subprocess
import platform


# ─── SERVICIO REAL ────────────────────────────
class Ping:
    """Clase real que realiza pings."""

    def _do_ping(self, host: str, intentos: int = 10) -> None:
        param = "-n" if platform.system().lower() == "windows" else "-c"
        print(f"  [Ping] Realizando {intentos} intentos a '{host}'...")
        for i in range(1, intentos + 1):
            resultado = subprocess.run(
                ["ping", param, "1", host],
                capture_output=True, text=True
            )
            estado = "OK" if resultado.returncode == 0 else "FALLO"
            print(f"    Intento {i:02d}/{intentos}: {estado}")

    def execute(self, string: str) -> None:
        """Ping con control: solo acepta IPs que comiencen con '192.'"""
        if not string.startswith("192."):
            print(f"  [Ping.execute] ERROR: '{string}' no comienza con '192.' — bloqueado.")
            return
        print(f"  [Ping.execute] IP válida. Iniciando ping a '{string}'...")
        self._do_ping(string)

    def executefree(self, string: str) -> None:
        """Ping sin control de dirección — acepta cualquier host."""
        print(f"  [Ping.executefree] Sin restricciones. Ping a '{string}'...")
        self._do_ping(string)


# ─── PROXY ────────────────────────────────────
class PingProxy:
    """
    Proxy de Ping.
    - Si la IP es '192.168.0.254' → redirige a www.google.com via executefree.
    - Cualquier otro caso          → delega a Ping.execute() normalmente.
    """

    def __init__(self):
        self._ping = Ping()   # objeto real, oculto al cliente

    def execute(self, string: str) -> None:
        print(f"\n[PingProxy.execute] Solicitud para: '{string}'")
        if string == "192.168.0.254":
            print("  [PingProxy] IP especial → redirigiendo a www.google.com")
            self._ping.executefree("www.google.com")
        else:
            print("  [PingProxy] Delegando a Ping.execute()...")
            self._ping.execute(string)


# ─── CLIENTE ──────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  TP4 - Ejercicio 1: Patrón Proxy (Ping)")
    print("=" * 55)

    proxy = PingProxy()

    # Caso 1: IP especial → va a google.com
    proxy.execute("192.168.0.254")

    # Caso 2: IP válida → pasa a Ping.execute()
    proxy.execute("192.168.1.1")

    # Caso 3: IP inválida → Ping.execute() la bloquea
    proxy.execute("10.0.0.1")