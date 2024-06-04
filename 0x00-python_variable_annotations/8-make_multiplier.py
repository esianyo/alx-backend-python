#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
    multiplier (float): The multiplier to use.

    Returns:
    Callable[[float], float]: A function that takes a float and returns a float.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    
    return multiplier_function
