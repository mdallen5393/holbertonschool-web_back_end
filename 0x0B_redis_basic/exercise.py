#!/usr/bin/env python3
"""
Module which defines the Cache class using Redis
"""
import redis
import uuid
from typing import Union

class Cache:
    """Defines a Redis cache"""
    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
