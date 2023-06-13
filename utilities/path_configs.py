import os
from pathlib import Path
from configparser import ConfigParser
import warnings


def get_path_to_file(*args: tuple) -> str:
    """Get the file path of the file by providing where is situated"""

    if len(args) < 1:
        raise ValueError("More than 1 argument is required")

    if not all([isinstance(item, str) for item in args]):
        raise TypeError("Arguments should be strings only")

    parent_dir = Path(__file__).parent.parent
    values = ' '.join(map(str, args))

    return os.path.join(parent_dir, *values.split())

class PathConfigs:

    parentDir = Path(__file__).parent.parent

    def __init_subclass__(cls, **kwargs):
        """This throws a deprecation warning on subclassing."""
        warnings.warn(f'{cls.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)
        super().__init_subclass__(**kwargs)

    def __init__(self, *args, **kwargs):
        """This throws a deprecation warning on initialization."""
        warnings.warn(f'{self.__class__.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)
        super().__init__(*args, **kwargs)

    @staticmethod
    def read_db_config(section):
        """ Read database configuration file and return a dictionary object
        :param filename: name of the configuration file
        :param section: section of database configuration
        :return: a dictionary of database parameters
        """

        warnings.warn("Function will be deprecated", DeprecationWarning)

        parser = ConfigParser()
        parser.read(PathConfigs.filePathToDBConfig)

        db = {}
        if parser.has_section(section):
            items = parser.items(section)
            for item in items:
                db[item[0]] = item[1]
        else:
            raise Exception('{0} not found in the {1} file'.format(section, PathConfigs.filePathToDBConfig))
        return db

    path_to_local_chrome_driver="C:\seleniumdrivers\chromedriver.exe"
    path_to_chrome_driver=os.path.join(parentDir,'drivers','chromedriver.exe')
    path_to_chrome_driver_pipeline=os.path.join(parentDir,'drivers','chromedriver')
    path_to_firefox_driver=os.path.join(parentDir,'drivers','geckodriver.exe')
    path_to_ie_driver=os.path.join(parentDir,'drivers','chromedriver.exe')
    path_to_config_file=os.path.join(parentDir,'config','config.ini')
