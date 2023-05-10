#!/usr/bin/env python3
"""
Coroutine that executes `async_comprehension` four times
in parallel using `asyncio.gather` and returns the total
runtime.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes `async_comprehension` four times and returns
    the total runtime.
    """
    start: float = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    return (time.time() - start)
