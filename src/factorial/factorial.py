#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
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

# Programa principal: verifica si hay argumento, si no lo pide
if len(sys.argv) < 2:
    entrada = input("Ingrese un número o rango (ej: 5, 4-8): ")
else:
    entrada = sys.argv[1]

# Verificar si es un rango (tiene guión)
if "-" in entrada:
    # Separar por el guión
    partes = entrada.split("-")
    inicio = int(partes[0])
    fin = int(partes[1])
    # Calcular factorial para cada número en el rango
    for numero in range(inicio, fin + 1):
        print("Factorial", numero, "! es", factorial(numero))
else:
    # Es un solo número
    num = int(entrada)
    print("Factorial", num, "! es", factorial(num))