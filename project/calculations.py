# calculator/calculations.py
# calculator/calculations.py

"""Provide sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
"""

def add(a, b):
    """Computes and  Returns the sum of `a` and `b`.

    Examples:
        >>> add(1, 8)
        9.0
        >>> add(3, 4)
        7.0

    Args:
        a (float): The first addend.
        b (float): The second addend.

    Returns:
        float:The sum of the two addends `a` and `b`.
     """
    return float(a+b)
