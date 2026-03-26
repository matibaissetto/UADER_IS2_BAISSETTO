#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número o rango de números                    *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Modificaciones: Maty Baissetto - Marzo 2026                             *
#*-------------------------------------------------------------------------*
import sys

def factorial(num):
    """
    Calcula el factorial de un número entero no negativo.
    Si el número es negativo, muestra error y retorna 0.
    Si el número es 0, retorna 1.
    Para números positivos, calcula el producto de 1 hasta el número.
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
    
    # Calcula y muestra el factorial para cada número en el rango
    for numero in range(inicio, fin + 1):
        print("Factorial", numero, "! es", factorial(numero))

else:
    # Es un solo número, no es rango
    num = int(entrada)
    print("Factorial", num, "! es", factorial(num))