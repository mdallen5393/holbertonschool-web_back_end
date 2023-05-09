#!/usr/bin/env python3
"""
Async routine that takes two arguments which spawns
`wait_random` `n` times with the specified `max_delay`.
It returns the list of all the delays in ascending
order.
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that calls `n` instances of wait_random.
    """
    wait_list: List = []
    for _ in range(n):
        await wait_list.append(wait_random(max_delay))
    return wait_list
