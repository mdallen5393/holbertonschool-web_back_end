#!/usr/bin/env python3
"""Module containing basic API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Class used for basic authentication
    """
    def __init__(self):
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a User object
        """
        return None
