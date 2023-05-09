#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an integer
argument that waits for a random delay and returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay
    and eventually returns the delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
