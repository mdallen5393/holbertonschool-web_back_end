#!/usr/bin/env python3
"""
Function that takes in a list of integers and returns a
tuple containing each list value and the length of each
list value
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes a list and returns a tuple with
    each list item and the items length.
    """
    return [(i, len(i)) for i in lst]
