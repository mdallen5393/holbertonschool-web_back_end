#!/user/bin/env python3
"""DB module
"""
from typing import TypeVar
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        # self._engine = create_engine("sqlite:///a.db", echo=True)
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Adds a user to the Users database and returns the new User object
        """
        if not email:
            return None
        if not hashed_password:
            return None
        user: User = User()
        user.email = email
        user.hashed_password = hashed_password
        self._session.add(user)
        self._session.commit()
        return user