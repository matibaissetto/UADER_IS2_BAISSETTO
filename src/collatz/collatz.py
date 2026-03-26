#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* collatz.py                                                              *
#* calcula la conjetura de Collatz para números del 1 al 10000             *
#* y genera un gráfico de iteraciones                                      *
#* Maty Baissetto - Marzo 2026                                             *
#*-------------------------------------------------------------------------*
import matplotlib.pyplot as plt

def iteraciones_collatz(n):
    """
    Calcula la cantidad de iteraciones que tarda un número en llegar a 1
    siguiendo la conjetura de Collatz.
    
    Parámetros:
    n (int): número inicial
    
    Retorna:
    int: cantidad de iteraciones
    """
    iteraciones = 0
    
    while n != 1:
        if n % 2 == 0:
            # Si es par, se divide por 2
            n = n // 2
        else:
            # Si es impar, se multiplica por 3 y se suma 1
            n = 3 * n + 1
        iteraciones += 1
    
    return iteraciones

# ------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------

print("Calculando iteraciones de Collatz para números del 1 al 10000...")

# Listas para el gráfico
numeros = []      # números iniciales (eje Y)
iteraciones = []  # cantidad de iteraciones (eje X)

# Calcular para cada número del 1 al 10000
for n in range(1, 10001):
    if n % 1000 == 0:
        print(f"Procesando... {n}/10000")
    
    numeros.append(n)
    iteraciones.append(iteraciones_collatz(n))

print("¡Cálculo completado! Generando gráfico...")

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.scatter(iteraciones, numeros, s=1, alpha=0.5, c='blue')
plt.xlabel("Número de iteraciones")
plt.ylabel("Número inicial (n)")
plt.title("Conjetura de Collatz: iteraciones para números del 1 al 10000")
plt.grid(True, alpha=0.3)

# Mostrar el gráfico
plt.show()

print("Gráfico cerrado. Programa finalizado.")