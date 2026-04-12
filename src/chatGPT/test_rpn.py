"""
=========================================================
Test suite RPN
=========================================================
"""

import unittest
from RPN import evaluate, RPNError


class TestRPN(unittest.TestCase):

    # ---------------- BASICAS ----------------
    def test_suma(self):
        self.assertEqual(evaluate("3 4 +"), 7)

    def test_resta(self):
        self.assertEqual(evaluate("10 2 -"), 8)

    def test_mult(self):
        self.assertEqual(evaluate("3 5 *"), 15)

    def test_div(self):
        self.assertEqual(evaluate("8 2 /"), 4)

    # ---------------- FLOAT ----------------
    def test_float(self):
        self.assertAlmostEqual(evaluate("2.5 2 *"), 5.0)

    # ---------------- PILA ----------------
    def test_dup(self):
        self.assertEqual(evaluate("5 dup *"), 25)

    def test_swap(self):
        self.assertEqual(evaluate("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(evaluate("3 4 drop"), 3)

    # ---------------- FUNCIONES ----------------
    def test_sqrt(self):
        self.assertEqual(evaluate("9 sqrt"), 3)

    def test_sin(self):
        self.assertAlmostEqual(evaluate("90 sin"), 1, places=5)

    def test_pi(self):
        self.assertAlmostEqual(evaluate("pi"), 3.14159, places=3)

    # ---------------- ERRORES ----------------
    def test_division_cero(self):
        with self.assertRaises(RPNError):
            evaluate("3 0 /")

    def test_token_invalido(self):
        with self.assertRaises(RPNError):
            evaluate("3 4 &")

    def test_pila_insuficiente(self):
        with self.assertRaises(RPNError):
            evaluate("3 +")

    def test_resultado_final(self):
        with self.assertRaises(RPNError):
            evaluate("3 4")


if __name__ == "__main__":
    unittest.main()