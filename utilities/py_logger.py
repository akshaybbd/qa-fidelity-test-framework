import logging

from utilities.path_configs import get_path_to_file

formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
log_file =get_path_to_file('logs','automation.log')
#PathConfigs.path_to_log_file_2

def get_file_handler() -> logging.FileHandler:
    """
    Setting up logger file and the formatter
    :returns: The file handler object
    """

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    return file_handler

def get_console_handler() -> logging.FileHandler:
    """Setting up a logger for console
    :returns: The file handler object
    """

    console_formatter = logging.Formatter('%(asctime)s - [%(name)s] - %(levelname)s - %(message)s', '%H:%M:%S')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    return console_handler


def get_logger(logger_name=__name__, console: str = False):
    """
    Setting up the logger, adding levels and handlers
    :returns: the logger object
    """

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    if console:
        logger.addHandler(get_console_handler())

    logger.addHandler(get_file_handler())

    logger.propagate = False

    return logger