# PROJECT: Python - Async

AUTHOR: Matthew Allen

## TASKS

### 0. The basics of async - `0-main.py`, `0-basic_async_syntax.py`

An asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and max_delay (included and float value) seconds and eventually returns it.

Uses the `random` module.

### 1. Let's execute multiple coroutines at the same time using async - `1-main.py`, `1-concurrent_coroutines.py`

Using `wait_random` from the previous task, this file contains an async routine called `wait_n` that takes in two int arguments (in this order): `n` and `max_delay`, and spawns `wait_random` `n` times with the specified `max_delay`.

`wait_n` returns the list of all the delays as floats, in ascending order, without using `sort()`.

### 2. Measure the runtime - `2-main.py`, `2-measure_runtime.py`

Using the previous `wait_n` function, this file contains a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n` as a float, using the `time` module to measure approximate elapsed time.

### 3. Tasks - `3-main.py`, `3-tasks.py`

Using the previous `wait_random` function, this file contains a function `task_wait_random` which takes an integer `max_delay` and returns an `asyncio.Task`.

### 4. Tasks - `4-main.py`, `4-tasks.py`

Function `task_wait_n` that is nearly identical to `wait_n`, but calls `task_wait_random` instead.
