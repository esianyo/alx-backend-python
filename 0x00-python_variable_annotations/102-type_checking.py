#!/usr/bin/env python3
from typing import Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Zooms in on an array by repeating each element a specified number of times.

    Args:
    - lst (Tuple[int, ...]): The input tuple to zoom in on.
    - factor (int): The factor by which to zoom in. Default is 2.

    Returns:
    - Tuple[int, ...]: The zoomed-in tuple.
    """
    zoomed_in: Tuple[int, ...] = tuple(item for item in lst for i in range(factor))
    return zoomed_in
