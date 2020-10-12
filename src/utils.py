"""
`utils.py` has several methods and constants that don't belong to any specific object/class.
They exist here so that they can be used multiple times without recursive imports.
"""

import requests

# sourced from https://www.wikiwand.com/en/Letter_frequency
RELATIVE_FREQUENCY_IN_THE_ENGLISH_LANGUAGE_TEXT: dict = {
    'A': 0.082, 'B': 0.015,
    'C': 0.028, 'D': 0.043, 'E': 0.13, 'F': 0.022, 'G': 0.02, 'H': 0.061,
    'I': 0.07, 'J': 0.0015, 'K': 0.0077, 'L': 0.04, 'M': 0.024, 'N': 0.067,
    'O': 0.075, 'P': 0.019, 'Q': 0.00095, 'R': 0.06, 'S': 0.063, 'T': 0.091,
    'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015, 'Y': 0.02, 'Z': 0.00074,
}

# sourced from https://www.wikiwand.com/en/Letter_frequency
RELATIVE_FREQUENCY_IN_THE_ENGLISH_LANGUAGE_DICTIONARIES: dict = {
    'A': 0.078, 'B': 0.02,
    'C': 0.04, 'D': 0.038, 'E': 0.11, 'F': 0.014, 'G': 0.03, 'H': 0.023,
    'I': 0.086, 'J': 0.0021, 'K': 0.0097, 'L': 0.053, 'M': 0.027, 'N': 0.072,
    'O': 0.061, 'P': 0.028, 'Q': 0.0019, 'R': 0.073, 'S': 0.087, 'T': 0.067,
    'U': 0.033, 'V': 0.01, 'W': 0.0091, 'X': 0.0027, 'Y': 0.016, 'Z': 0.0044,
}


def make_request(url: str) -> str:
    response = requests.get(url, headers={"User-Agent": ""})
    return response.text


def create_frequency_map(text: str, map: dict, sort=False, sort_desc=True) -> dict:
    '''
    Counts the occurrences of each character in the string.
    Returns the result as an unsorted map.
    '''

    if type(map) is not dict or map is None:
        map: dict = {}

    for character in text:
        if character in map:
            # increment the count by one
            map[character] += 1
        else:
            # adds the new character to the map
            map[character] = 1

    # Sorts the dictionary
    if sort is True:
        map = {
            letter: count
            for letter, count in sorted(
                map.items(),
                key=lambda letter_m: letter_m[1],
                reverse=sort_desc
            )
        }
    return map


def assert_char_key_alphabet(char: str, key: str, alphabet: str) -> None:
    """An assertion on the type and length of the `char`, `key`, and `alphabet`."""
    # Assert char and key are the characters
    if len(char) > 1 or len(key) > 1 or len(alphabet) != 26:
        print("Please provide a single character. You provided:")
        print("char: {}".format(char))
        print("key:  {}".format(key))
        raise AssertionError()
    elif type(char) is not str or type(key) is not str or type(alphabet) is not str:
        print("Not the correct type.")
        raise TypeError()


def encrypt_letter(char: str, key: str, alphabet: str) -> str:
    """
    Encrypt an individual letter with a given `char`, `key`, and `alphabet`.

    ```txt
    E = (P + K) mod 26
    ```
    """

    assert_char_key_alphabet(char, key, alphabet)

    if char not in alphabet:
        return char

    p = ord(char) - 65  # plaintext value
    k = ord(key) - 65   # key value
    e = (p + k) % 26    # encrypted value

    enc_char = alphabet[e]
    return enc_char


def decrypt_letter(char: str, key: str, alphabet: str) -> str:
    """
    Decrypt an individual letter with a given `char`, `key`, and `alphabet`.

    ```txt
    P = (E - K + 26) mod 26
    ```
    """

    assert_char_key_alphabet(char, key, alphabet)

    # Takes care of non alpha characters
    if char not in alphabet:
        return char

    # a value of 0 - 25
    e = alphabet.index(char)

    # a value 0 - 25
    k = ord(key) - 65

    # p
    p = (e - k + 26) % 26 + 65

    return chr(p)


def remove_not_in_alphabet(text, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    """
    Removes non-alphabetic characters (including whitespace | [`a-zA-Z`]),
    can also provide own alphabet.
    """

    # Assert text
    if type(text) is not str:
        raise AssertionError()

    trimmed_text = ""
    for letter in text:
        if letter in alphabet:
            trimmed_text = trimmed_text + letter

    return trimmed_text
