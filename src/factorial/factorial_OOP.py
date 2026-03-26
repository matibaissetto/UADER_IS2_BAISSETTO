#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                       *
#* calcula el factorial de un número o rango usando una clase             *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Modificaciones: Maty Baissetto - Marzo 2026                             *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    """
    Clase para calcular factoriales.
    Contiene un método run() que calcula factoriales en un rango.
    """
    
    def __init__(self):
        """
        Constructor de la clase.
        No necesita inicializar nada por ahora.
        """
        pass
    
    def run(self, min, max):
        """
        Calcula y muestra el factorial de cada número entre min y max.
        
        Parámetros:
        min (int): número inicial del rango
        max (int): número final del rango
        """
        for numero in range(min, max + 1):
            print("Factorial", numero, "! es", self.factorial(numero))
    
    def factorial(self, num):
        """
        Calcula el factorial de un número entero no negativo.
        
        Parámetros:
        num (int): número a calcular
        
        Retorna:
        int: factorial del número, o 0 si es negativo
        """
        if num < 0:
            print("Factorial de un número negativo no existe")
            return 0
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact


# ------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------

# Crear un objeto de la clase Factorial
calculadora = Factorial()

# Verifica si se pasó un argumento al ejecutar el programa
if len(sys.argv) < 2:
    # No hay argumento: lo solicitamos por teclado
    entrada = input("Ingrese un número o rango (ej: 5, 4-8, -10, 5-): ")
else:
    # Hay argumento: lo tomamos de la línea de comandos
    entrada = sys.argv[1]

# Verifica si la entrada contiene un guión (es un rango)
if "-" in entrada:
    # Separa la entrada en dos partes usando el guión como separador
    partes = entrada.split("-")
    
    # Caso 1: "-10" (no hay inicio) -> desde 1 hasta el número
    if partes[0] == "":
        inicio = 1
        fin = int(partes[1])
    
    # Caso 2: "5-" (no hay fin) -> desde el número hasta 60
    elif partes[1] == "":
        inicio = int(partes[0])
        fin = 60
    
    # Caso 3: "4-8" (rango completo) -> desde inicio hasta fin
    else:
        inicio = int(partes[0])
        fin = int(partes[1])
    
    # Usar el método run de la clase para calcular los factoriales
    calculadora.run(inicio, fin)

else:
    # Es un solo número, no es rango
    num = int(entrada)
    # Para un solo número, llamamos al método factorial directamente
    print("Factorial", num, "! es", calculadora.factorial(num))