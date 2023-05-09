#!/usr/bin/env python3
"""
Function altered from wait_n to call task_wait_random
instead.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Function that calls `n` instances of wait_random.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    wait_list = []
    for task in asyncio.as_completed(tasks):
        result = await task
        wait_list.append(result)
    return wait_list
