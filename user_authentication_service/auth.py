#!/usr/bin/env python3
"""Module that contains the Auth class"""
from user import User
from db import DB
from bcrypt import hashpw, gensalt
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Hashes the password and saves the user to the database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
        if user:
            raise ValueError(f"User {email} already exists.")
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user


def _hash_password(password: str) -> bytes:
    """Returns a salted hash of the input password"""
    encoded_password = password.encode('utf-8')
    return hashpw(encoded_password, gensalt())
