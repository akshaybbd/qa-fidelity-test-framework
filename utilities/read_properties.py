# created by Abhijeet Thorat at 2023-06-13 17:46.
#

import configparser
import warnings
from utilities.path_configs import PathConfigs
from utilities.path_configs import get_path_to_file
from utilities.py_logger import get_logger

warnings.simplefilter('always', DeprecationWarning)
logger = get_logger(logger_name=__name__)
config=configparser.RawConfigParser()
config.read(PathConfigs.path_to_config_file)

class ReadConfig():
    """Reading file configs. To be deprecated"""

    def __init_subclass__(cls, **kwargs):
        """This throws a deprecation warning on subclassing."""
        warnings.warn(f'{cls.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)
        super().__init_subclass__(**kwargs)

    def __init__(self, *args, **kwargs):
        """This throws a deprecation warning on initialization."""
        warnings.warn(f'{self.__class__.__name__} will be deprecated.', DeprecationWarning, stacklevel=2)
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_reward_management_host():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        host = config.get('rewards db', 'host')
        user = config.get('rewards db', 'user')
        password = config.get('rewards db', 'password')
        database = config.get('rewards db', 'database')

        return {"host": host, "user": user, "password": password, "database": database}

    @staticmethod
    def get_api_bearer_token():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        return config.get('token', 'bearer_token_api')


    @staticmethod
    def get_magento_data():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        host_name = config.get('magento', 'host_name')

        magento_data = {
            "host_name": config.get('magento', 'host_name'),
            "api_key": config.get('magento', 'api_key'),
            "bearer_token": config.get('magento', 'bearer_token'),
            "access_token": config.get('magento', 'access_token'),
            "Store": config.get('magento', 'Store')
        }

        return magento_data


    @staticmethod
    def get_application_url():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        url=config.get('common info','base_url')
        return url


    @staticmethod
    def get_application_username():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        username = config.get('common info', 'username')
        return username


    @staticmethod
    def get_application_password():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        password=config.get('common info','password')
        return password


    @staticmethod
    def get_api_gateway_hostname_test():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        dev_environment = config.get('api gateway', 'dev_environment')
        return dev_environment


    @staticmethod
    def get_api_gateway_hostname_test():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        test_environment = config.get('api gateway', 'test_environment')
        return test_environment


    @staticmethod
    def get_bearer_token_auth_test_url():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        bearer_token_auth_test_url = config.get('bearer_token', 'bearer_token_auth_test_url')
        return bearer_token_auth_test_url


    @staticmethod
    def get_bearer_token_auth_dev_url():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        bearer_token_auth_dev_url = config.get('bearer_token', 'bearer_token_auth_dev_url')
        return bearer_token_auth_dev_url


    @staticmethod
    def get_advance_me_reward_reservation_api_path():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        advance_me_reward_reservation_path = config.get('api path', 'advance_me_reward_reservation')
        return advance_me_reward_reservation_path


    @staticmethod
    def get_advance_me_reward_cancellation_api_path():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        advance_me_reward_cancellation_api_path = config.get('api path', 'advance_me_reward_cancellation')
        return advance_me_reward_cancellation_api_path


    @staticmethod
    def get_advance_me_reward_commitment_api_path():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        advance_me_reward_commitment_api_path = config.get('api path', 'advance_me_reward_commitment')
        return advance_me_reward_commitment_api_path


    @staticmethod
    def get_advance_me_redemption_history_api_path():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        advance_me_redemption_history_api_path = config.get('api path', 'advance_me_redemption_history')
        return advance_me_redemption_history_api_path


    @staticmethod
    def get_j4y_data_elgibility_rules_api_path():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        j4y_data_elgibility_rules_api_path = config.get('api path', 'j4y_data_eligibility_rules')
        return j4y_data_elgibility_rules_api_path


    @staticmethod
    def get_pulse_db_host():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        pulse_db_host = config.get('pulse db connections', 'host')
        return pulse_db_host


    @staticmethod
    def get_pulse_db_host():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        pulse_db_host = config.get('pulse db connections', 'host')
        return pulse_db_host


    @staticmethod
    def get_pulse_db_port():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        pulse_db_port = config.get('pulse db connections', 'port')
        return pulse_db_port


    @staticmethod
    def get_pulse_db_user():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        pulse_db_user = config.get('pulse db connections', 'user')
        return pulse_db_user


    @staticmethod
    def get_pulse_db_password():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        pulse_db_password = config.get('pulse db connections', 'password')
        return pulse_db_password


    @staticmethod
    def get_pulse_db_name():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        pulse_db_name = config.get('pulse db connections', 'name')
        return pulse_db_name


    @staticmethod
    def get_ussd_simulator_username():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        ussd_simulator_username = config.get('ussd simulator', 'username')
        return ussd_simulator_username


    @staticmethod
    def get_ussd_simulator_password():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        ussd_simulator_password = config.get('ussd simulator', 'password')
        return ussd_simulator_password


    @staticmethod
    def get_vodabucks_reload_api_path():
        warnings.warn("Function will be deprecated", DeprecationWarning)

        advance_me_reward_reservation_path = config.get('api path', 'vodabucks_reload')
        return advance_me_reward_reservation_path


def interpret_config_file(path: str = get_path_to_file('config', 'config.ini')):
    """Read and return a config parser object"""

    config_object = configparser.ConfigParser()

    try:
        config_object.read(path)
    except Exception:
        logger.exception("Error reading the config file")
        return None

    return config_object


def extract_specific_data(results: dict = None, section: str = None, option: str = None):
    """Extract specific data when specified section and options are visible"""

    if section is not None and option is None:
        return results[section]
    if section is not None and option is not None:
        return results[section][option]

    return results


def read_config_file(
        path_to_config: str = get_path_to_file('config', 'config.ini'),
        section: str = None,
        option: str = None
        ):
    """Read a config file. With an option fields of option and section"""
    config_object = interpret_config_file(path=path_to_config)
    results = {}

    for section_config in config_object.sections():
        section_dict = {}

        for option_config in config_object.options(section_config):

            try:
                section_dict[option_config] = config_object.get(section_config, option_config)
            except Exception:
                logger.exception(f"Error reading option {option} in section {section}")

        results[section_config] = section_dict

    return extract_specific_data(results=results, section=section, option=option)
