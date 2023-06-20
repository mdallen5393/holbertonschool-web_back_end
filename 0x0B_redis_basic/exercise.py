#!/usr/bin/env python3
"""
Module which defines the Cache class using Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    """Defines a Redis cache"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        value = self._redis.get(key)
        if value is not None and fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        value = self.get(key, str)
        return value

    def get_int(self, key: str) -> Optional[int]:
        value = self.get(key, int)
        return value
