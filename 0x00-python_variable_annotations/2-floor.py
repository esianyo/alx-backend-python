#!/usr/bin/env python3
"""
This module contains a function that returns the
floor of a float with type annotations.
"""
import math


def floor(n: float) -> int:
    """
    Return the floor of a float.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The floor of the float.
    """
    return math.floor(n)
