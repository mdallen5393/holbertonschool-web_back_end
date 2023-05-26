#!/usr/bin/env python3
"""Module that contains SessionAuth class definition."""
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Allows 'in-memory' Session ID storing"""
    pass
