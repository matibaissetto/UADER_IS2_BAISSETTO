"""
=========================================================
RPN.py
Calculadora en notación Reverse Polish Notation (RPN)
Versión final con mejoras sugeridas por ChatGPT
=========================================================
"""

import math
import sys
import operator


# =========================================================
# EXCEPCIÓN PERSONALIZADA
# =========================================================
class RPNError(Exception):
    pass


# =========================================================
# MEJOR DETECCIÓN DE NÚMEROS
# =========================================================
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


# =========================================================
# POP SEGURO DE PILA
# =========================================================
def pop_stack(stack):
    if not stack:
        raise RPNError("Pila insuficiente")
    return stack.pop()


# =========================================================
# OPERADORES BINARIOS
# =========================================================
binary_ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}


# =========================================================
# FUNCIÓN PRINCIPAL
# =========================================================
def evaluate(expression):
    stack = []
    memory = {}  # se mantiene para compatibilidad futura

    tokens = expression.split()

    for token in tokens:

        # ---------------- NUMEROS ----------------
        if is_number(token):
            stack.append(float(token))

        # ---------------- OPERADORES BÁSICOS ----------------
        elif token in binary_ops:
            b = pop_stack(stack)
            a = pop_stack(stack)

            if token == "/" and b == 0:
                raise RPNError("División por cero")

            stack.append(binary_ops[token](a, b))

        # ---------------- PILA ----------------
        elif token == "dup":
            if not stack:
                raise RPNError("Pila insuficiente")
            stack.append(stack[-1])

        elif token == "swap":
            if len(stack) < 2:
                raise RPNError("Pila insuficiente")
            stack[-1], stack[-2] = stack[-2], stack[-1]

        elif token == "drop":
            pop_stack(stack)

        # ---------------- FUNCIONES ----------------
        elif token == "sqrt":
            a = pop_stack(stack)
            if a < 0:
                raise RPNError("Dominio inválido")
            stack.append(math.sqrt(a))

        elif token == "sin":
            a = pop_stack(stack)
            stack.append(math.sin(math.radians(a)))

        # ---------------- CONSTANTE ----------------
        elif token == "pi":
            stack.append(math.pi)

        # ---------------- ERROR ----------------
        else:
            raise RPNError(f"Token inválido: {token}")

    if len(stack) != 1:
        raise RPNError("Expresión inválida")

    return stack[0]


# =========================================================
# EJECUCIÓN DESDE CONSOLA
# =========================================================
def main():
    expression = " ".join(sys.argv[1:])
    try:
        print(evaluate(expression))
    except RPNError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()