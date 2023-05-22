#!/usr/bin/env bash
"""
Contains a `hash_password` function that returns a salted,
hashed password, which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> None:
    """
    Function that takes in a password string and returns
    a salted, hashed password, which is a byte string.
    """
    pass

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether the provided password matches the
    hashed password.
    """
    pass
