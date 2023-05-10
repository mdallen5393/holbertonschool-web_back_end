#!/usr/bin/env python3
"""
Function that measures the total execution time for
`wait_n(n, max_delay)`, and returns `total_time / n`
as a float.
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Returns mean time per task taken for `wait_n` to
    to return.
    """
    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    return ((time.time() - start) / n)
