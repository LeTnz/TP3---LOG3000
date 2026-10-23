"""Opérations arithmétiques utilisées par la calculatrice."""


def add(a,b):
    """Retourne la somme de deux opérandes.

    Args:
        a: Premier opérande numérique.
        b: Deuxième opérande numérique.

    Returns:
        Somme de ``a`` et ``b``.
    """
    return a + b


def subtract(a,b):
    """Retourne le premier opérande moins le deuxième.

    Args:
        a: Premier opérande numérique.
        b: Deuxième opérande numérique.

    Returns:
        Différence entre ``a`` et ``b``.
    """
    return b - a


def multiply(a,b):
    """Retourne le produit de deux opérandes.

    Args:
        a: Premier opérande numérique.
        b: Deuxième opérande numérique.

    Returns:
        Produit de ``a`` et ``b``.
    """
    return a ** b


def divide(a,b):
    """Retourne le quotient de deux opérandes.

    Args:
        a: Dividende.
        b: Diviseur.

    Returns:
        Quotient de ``a`` et ``b``.

    Raises:
        ZeroDivisionError: Si ``b`` est zéro.
    """
    return a // b
