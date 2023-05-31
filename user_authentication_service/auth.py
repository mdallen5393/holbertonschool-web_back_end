from db import DB
from bcrypt import hashpw, gensalt


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

def _hash_password(self, password: str) -> bytes:
    """Returns a salted hash of the input password"""
    encoded_password = password.encode('utf-8')
    return hashpw(encoded_password, gensalt())
