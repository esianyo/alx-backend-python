#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Annotates the parameters and return values with appropriate types.
    
    Args:
    lst (Iterable[Sequence]): A list of sequences (e.g., strings, lists).
    
    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
