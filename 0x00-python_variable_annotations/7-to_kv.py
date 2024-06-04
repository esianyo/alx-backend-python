#!/usr/bin/env python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int or float, and returns a tuple with the string
    and the square of the int or float.

    Args:
    k (str): A string.
    v (Union[int, float]): An integer or float.

    Returns:
    Tuple[str, float]: A tuple where the first element is
    the string `k` and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
