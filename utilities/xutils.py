# created by Abhijeet Thorat at 2023-06-13 20:55.
#

import json
import os
import requests
import numpy as np
import pandas as pd

from utilities.py_logger import get_logger

logger = get_logger(logger_name=__name__)

def get_data_from_datasheet(test_input_datasheet: str, sheet_name: str) -> pd.DataFrame:
    """Read data from a datasheet"""

    path_to_file = os.path.join(test_input_datasheet)
    test_data_df = pd.read_excel(path_to_file, dtype=object, sheet_name=sheet_name, engine='openpyxl')
    return test_data_df


def remove_none_values(json_body: dict) -> dict:
    """Remove None values recursively from all of the dictionaries, tuples, lists, sets"""

    if isinstance(json_body, dict):
        for key, value in list(json_body.items()):
            if isinstance(value, (list, dict, tuple, set)):
                json_body[key] = remove_none_values(value)
            elif value is None or key is None:
                del json_body[key]

    elif isinstance(json_body, (list, set, tuple)):
        json_body = type(json_body)(remove_none_values(item) for item in json_body if item is not None)

    return json_body


def extract_test_data_from_dataframe(filtered_test_data: pd.DataFrame = None) -> dict:
    """Construct a dictionary of test data from a datasheet or database"""

    try:
        test_data = {}
        column_names = list(filtered_test_data)

        for key in column_names:
            test_data.update({key: filtered_test_data[key].replace(np.nan, " ").tolist()[0]})

        return test_data

    except KeyError:
        logger.exception("Key does not exist")


def pretty_json(response_body: requests) -> str:
    """
    Formats a response object to a json

    :param: response object
    :returns: json formatted response with 4 tab spaces
    """
    response = response_body.json()
    json_body = json.dumps(response, indent=4, sort_keys=True)

    return json_body


def pretty_dictionary(dictionary: dict) -> str:
    """Formats a dictionary properly"""

    if not isinstance(dictionary, dict):
        raise TypeError(f"A type of {type(dictionary)}  was provided. Pass a `dict` value")

    return json.dumps(dictionary, sort_keys=True, indent=4)