"""Tests qui révèlent les bogues de l'implémentation initiale."""

import unittest

from app import app, calculate
from operators import add, divide, multiply, subtract


class OperatorTests(unittest.TestCase):
    """Vérifie le comportement attendu de chaque opération arithmétique."""

    def test_addition(self):
        """Vérifie que l'addition retourne la somme des deux opérandes."""
        self.assertEqual(add(2, 3), 5)

    def test_subtraction(self):
        """Vérifie que la soustraction respecte l'ordre des opérandes."""
        self.assertEqual(subtract(8, 3), 5)

    def test_multiplication(self):
        """Vérifie que la multiplication retourne un produit et non une puissance."""
        self.assertEqual(multiply(4, 3), 12)

    def test_division(self):
        """Vérifie que la division retourne un quotient réel."""
        self.assertEqual(divide(7, 2), 3.5)

    def test_division_by_zero_is_rejected(self):
        """Vérifie que la division par zéro est refusée explicitement."""
        with self.assertRaises((ValueError, ZeroDivisionError)):
            divide(1, 0)


class ApplicationTests(unittest.TestCase):
    """Vérifie l'analyse des expressions et la route Flask principale."""

    def test_calculate_supported_expressions(self):
        """Vérifie que l'analyseur utilise correctement chaque opérateur."""
        self.assertEqual(calculate("2+3"), 5)
        self.assertEqual(calculate("8-3"), 5)
        self.assertEqual(calculate("4*3"), 12)
        self.assertEqual(calculate("7/2"), 3.5)

    def test_invalid_expression_is_rejected(self):
        """Vérifie qu'une expression mal formée provoque une erreur."""
        with self.assertRaises(ValueError):
            calculate("2+3*4")

    @classmethod
    def setUpClass(cls):
        """Crée un client de test Flask pour vérifier la route."""
        app.config["TESTING"] = True
        cls.client = app.test_client()

    def test_get_renders_page(self):
        """Vérifie que GET / retourne la page de la calculatrice."""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_post_renders_result(self):
        """Vérifie que POST / affiche le résultat de l'expression soumise."""
        response = self.client.post("/", data={"display": "6*7"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"42", response.data)


if __name__ == "__main__":
    unittest.main()
