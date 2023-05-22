#!/usr/bin/env python3
"""
Contains a function that returns the log message obfuscated.
"""
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """
    Function that returns the log message obfuscated.
    """
    pass
