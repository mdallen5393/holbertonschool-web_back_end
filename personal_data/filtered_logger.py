#!/usr/bin/env python3
"""
Contains a function that returns the log message obfuscated.
"""
import logging
import re
from typing import List

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Filters values in incoming log records using `filter_datum`.
        """
        record.msg = filter_datum(self.fields, RedactingFormatter.REDACTION,
                                  record.msg, RedactingFormatter.SEPARATOR)
        return super().format(record)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Function that returns the log message obfuscated.
    """
    obfuscated_str: str = message
    for field in fields:
        obfuscated_str = re.sub('{}=.*?(?={})'.format(field, separator),
                                '{}={}'.format(field, redaction),
                                obfuscated_str)
    return obfuscated_str

def get_logger() -> logging.Logger:
    """
    Function that creates a Logger object and obfuscates the appropriate
    data.
    """
    new_logger: logging.Logger = logging.getLogger('user_data')
    new_logger.setLevel(logging.INFO)
    new_logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter()
    handler.setFormatter(formatter)
    new_logger.addHandler(handler)
    return new_logger
