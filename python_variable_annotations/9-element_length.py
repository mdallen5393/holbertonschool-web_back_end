#!/usr/bin/env python3
"""
Function that does something with someone that defies my
understanding entirely.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Magic.
    """
    return [(i, len(i)) for i in lst]
