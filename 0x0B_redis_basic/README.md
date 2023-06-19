# PROJECT: Redis basic

AUTHOR: Matthew Allen

## TASKS

### 0. Writing strings to Redis - `main.py`, `exercise.py`

Creates a `Cache` class. In the `__init__` method, stores an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flushes the instance using `flushdb`.

Creates a `store` method that takes a `data` argument and returns a string.  The method generates a random key (e.g. using `uuid`), stores the input data in Redis using the random key and returns the key.

`store` is type annotated.

### 1. Reading from Redis and recovering original type - `exercise.py`

Creates a `get` method that takes a `key` string argument and an optional `Callable` argument named `fn`.  This callable is used to convert the data back to the desired format.

Conserves the original `Redis.get` behavior if the key does not exist.

Implements `get_str` and `get_int` methods which automatically parameterize `Cache.get` with the correct conversion function.

### 2. Incrementing values - `2-main.py`, `exercise.py`

Implements a system to count how many times methods of the `Cache` class are called.

Above `Cache`, defines a `count_calls` decorator that takes a single `method Callable` argument and returns a `Callable`.

As a key, uses the qualified name of `method` using the `__qualname__` dunder method.

Creates and returns function that increments the count for that key every time the method is called and returns the value returned by the original method.

Uses `functool.wraps` to conserve the original function's name, docstring, etc.

`Cache.store` is decorated with `count_calls`.

### 3. Storing lists - `3-main.py`

Defines a `call_history` decorator to store the history of inputs and outputs for a particular function.

Everytime the original function is called, its input parameters will be added to one list in redis, and its output is stored into another list.

In `call_history`, the decorated function's qualified name is used and appended with `":inputs"` and `:outputs"`, which creates input and output list keys, respectively.

In the new function that the decorator returns, `rpush` is used to append the input arguments. `str(args)` is used to normalize, and `kwargs` are ignored.

The wrapped function is executed to retrieve the output and is stored using `rpush` in the `"...:outputs"` list.  Then the output is returned.

`Cache.store` is decarated with `call_history`.

### 4. Retrieving lists - `exercise.py`

Implements a `replay` function which displays the history of calls of a particular function.

Uses the keys generated in previous tasks to generate output.

Uses `lrange` and `zip` to loop over inputs and outputs.
