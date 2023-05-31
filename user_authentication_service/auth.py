#!/usr/bin/env python3
"""Module that contains the Auth class"""
from user import User
from db import DB
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


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

    def valid_login(self, email: str, password: str) -> bool:
        """Locates a user by email and checks whether the passwrod matches
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if user:
            encoded_password = password.encode('utf-8')
            if checkpw(encoded_password, user.hashed_password):
                return True
        return False


def _generate_uuid() -> str:
    """Generates and returns a string representation of a new UUID."""
    return str(uuid4())

def _hash_password(password: str) -> bytes:
    """Returns a salted hash of the input password"""
    encoded_password = password.encode('utf-8')
    return hashpw(encoded_password, gensalt())
