# created by Abhijeet Thorat at 2023-06-13 17:35.
#

import base64
import utilities.py_logger as py_logger

def encodeMessage(message):
    """Encoding a string with base64 encryption
    :params: an utf-8 string
    :returns: an encoded base64 string
    """

    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decodeMessage(base64_message):
    """Decoding a string with base64 decryption
    :params: an utf-8 string
    :returns: a decoded base64 string
    """

    base64_message = base64_message
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decodedString = message_bytes.decode('ascii')
    return decodedString
