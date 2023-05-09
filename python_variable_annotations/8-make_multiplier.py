#!/usr/bin/env python3
"""
Type-annotated function that takes a float `multiplier` as
argument and returns a function that multiplies a float by
`multiplier`.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def mult(num: float) -> float:
        return (num * multiplier)
    return mult
