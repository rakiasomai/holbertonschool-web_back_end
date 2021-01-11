#!/usr/bin/env python3
''' Personal Data '''

import logging
from typing import List
import re
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    ''' Redacting Formatter class '''
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        ''' fed init '''
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        ''' def format '''
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    ''' Returns the log message obfuscated '''
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}",
                         f'{field}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    ''' def logger '''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = logging.Formatter(RedactingFormatter(PII_FIELDS))
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    ''' def get deb '''
    cnx = mysql.connector.connection.MySQLConnection(
      user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
      password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
      host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
      database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return cnx
