# created by Abhijeet Thorat at 2023-06-13 17:38.
#

import logging
from utilities.path_configs import PathConfigs
from warnings import warn

class LogGen:
    """
    This logger class will be deprecated
    """

    def __init__(self) -> None:
        pass
        warn(f'{self.__class__.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)

    @staticmethod
    def loggen():
        warn(f'This method will be deprecated.', DeprecationWarning, stacklevel=2)

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename=PathConfigs.path_to_log_file_2, mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger
