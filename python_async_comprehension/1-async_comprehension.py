#!/usr/bin/env python3
"""
Coroutine that collects 10 random numbers using an
async comprehensing over `async_generator`, and returns
the 10 random numbers.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returns 10 numbers returned by `async_generator`.
    """
    return [num async for num in async_generator()]
