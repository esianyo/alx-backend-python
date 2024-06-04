#!/usr/bin/env python3
from typing import List, Tuple, Union


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Creates a list containing elements of the input tuple repeated 'factor' times.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The number of times to repeat each element. Defaults to 2.

    Returns:
        List[int]: A list with elements of the tuple repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in

array = (12, 72, 91)  # Should be a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
