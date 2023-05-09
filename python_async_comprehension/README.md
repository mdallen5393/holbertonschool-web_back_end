# PROJECT: Python - Async Comprehension

AUTHOR: Matthew Allen

## TASKS

### 0. Async Generator - `0-main.py`, `0-async_generator.py`

`async_generator` coroutine that takes no arguments and loops 10 times, each time asynchronously waiting 1 second, then yield a random number between 0 and 10.

Uses the `random` module.

### 1. Async Comprehensions - `1-main.py`, `1-async_comprehension.py`

Using `async_generator` from the previous task, this coroutine named `async_comprehension` takes no arguments and collects 10 random numbers using an async comprehensing over `async_generator`, then returns the 10 random numbers.

### 2. Run time for four parallel comprehensions - `2-main.py`, `2-measure_runtime.py`

Using `async_comprehension` from the previous task, this coroutine named `measure_runtime` executes `async_comprehension` four times in parallel using `asyncio.gather`.  It measures and returns the total runtime, which is roughly 10 seconds.
