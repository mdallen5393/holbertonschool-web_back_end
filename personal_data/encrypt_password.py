#!/usr/bin/env bash
"""
Contains a `hash_password` function that returns a salted,
hashed password, which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that takes in a password string and returns
    a salted, hashed password, which is a byte string.
    """
    encoded_password = password.encode('utf-8')
    return (bcrypt.hashpw(encoded_password, bcrypt.gensalt()))



def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether the provided password matches the
    hashed password.
    """
    if bcrypt.checkpw(password, hashed_password):
        return 
