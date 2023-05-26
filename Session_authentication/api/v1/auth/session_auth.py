#!/usr/bin/env python3
"""Module that contains SessionAuth class definition."""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Allows 'in-memory' Session ID storing"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a `user_id`"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method for retrieving a User ID"""
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)
