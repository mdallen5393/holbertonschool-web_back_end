#!/usr/bin/env python3
"""
Type-annotated function that takes a string `k` and an int
OR float `v` as arguments and returns a tuple.  The first
element of the fuple is the string `k`.  The second element
element is the square of the int/float `v` and is
annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a tuple containing the input string
    and the square of the input int or float.
    """
    return (k, float(v) ** 2)
