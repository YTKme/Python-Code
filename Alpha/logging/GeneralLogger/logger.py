"""Logger Module

This module implements a custom Logger.
"""

import logging
from pathlib import Path


# Log Level
CRITICAL = logging.CRITICAL
FATAL = logging.FATAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET

RECORD_FORMAT = '[%(name)s %(levelname)s %(asctime)s] %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ColorCode:
    """Color Code for logging"""
    
    NOTSET = '\x1b[0m'
    DEBUG = '\x1b[1;36m'
    INFO = '\x1b[38;21m'
    WARNING = '\x1b[33;21m'
    SUCCESS = '\x1b[1;32m'
    ERROR = '\x1b[31;21m'
    CRITICAL = '\x1b[31;47m'


class Logger(logging.Logger):
    """Logger class for AutoTools

    A Logger with predefined log format.
    """

    def __init__(self,
                 name: str,
                 level=NOTSET) -> None:
                # No UnionType yet
                #  level: int | str = NOTSET) -> None:
        """Constructor
        
        :param name: (str) the name of the logger
        :param level: (int) or (str) initialize the level of the logger
        """

        # Call super class
        super(Logger, self).__init__(name=name, level=level)

        # Initialize handler
        self.handler = logging.StreamHandler()
        self.handler.setLevel(level)
        self.handler.setFormatter(LoggerFormatter())
        self.addHandler(self.handler)


    def set_formatter(self,
                      record_format: str = RECORD_FORMAT,
                      date_format: str = DATE_FORMAT) -> None:
        """Set Formatter for Logger

        Enable user to set a different format for the log record and the
        log date.

        :param record_format: (str) the new format for the log record
        :param date_format: (str) the new format for the log date
        """

        self.removeHandler(self.handler)
        self.handler.setFormatter(LoggerFormatter(record_format=record_format,
                                                  date_format=date_format))
        self.addHandler(self.handler)



class LoggerFormatter(logging.Formatter):
    """Formatter for the Logger

    Define a custom Logger Formatter with color.
    """

    def __init__(self,
                 record_format: str = RECORD_FORMAT,
                 date_format: str = DATE_FORMAT) -> None:
        """Constructor

        :param log_format: (str) the log format for the Formatter
        :param date_format: (str) the date format for the Formatter
        """
        # Call super class
        super().__init__(fmt=record_format, datefmt=date_format)

        self.LEVEL_FORMAT = {
            logging.DEBUG: f'{ColorCode.DEBUG}{record_format}{ColorCode.NOTSET}',
            logging.INFO: f'{ColorCode.INFO}{record_format}{ColorCode.NOTSET}',
            logging.WARNING: f'{ColorCode.WARNING}{record_format}{ColorCode.NOTSET}',
            logging.ERROR: f'{ColorCode.ERROR}{record_format}{ColorCode.NOTSET}',
            logging.CRITICAL: f'{ColorCode.CRITICAL}{record_format}{ColorCode.NOTSET}'
        }

        self.date_format = date_format

    
    def format(self, record):
        """Format the specified record as text (redefined)

        :param record: (dict) the record to format, used for string
            formatting operation
        """
        log_format = self.LEVEL_FORMAT.get(record.levelno)
        formatter = logging.Formatter(fmt=log_format, datefmt=self.date_format)

        return formatter.format(record)
