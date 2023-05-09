#!/usr/bin/env python3
"""
Function that does things to stuff whilst defying my
understanding entirely.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Magic.
    """
    return [(i, len(i)) for i in lst]
