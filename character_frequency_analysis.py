import re
from vigenere_cipher import remove_not_in_alphabet


def _create_frequency_map(text: str, desc=True) -> dict:
    '''
    Counts the occurrences of each character in the string.
    Returns the result as an unsorted map.
    '''

    letter_map: dict = {}
    for character in text:
        if character in letter_map:
            # increment the count by one
            letter_map[character] += 1
        else:
            # adds the new character to the map
            letter_map[character] = 1

    # Sorts the dictionary
    letter_map = {
        letter: count
        for letter, count in sorted(
            letter_map.items(),
            key=lambda letter_m: letter_m[1],
            reverse=desc
        )
    }
    return letter_map


class CharacterFrequencyAnalyzer():
    """
    Used to analyze the characters of a given text based on an alphabet.\n
    Usage:\n
    ```python
    >>> s = "This is the source string ... exclamation mark!"
    >>> x = CharacterFrequencyAnalyzer(s, alphabet="A]{DEFGHI.KLMNO-QRSTUV!XYZ")
    >>> print
    ```
    """

    def __init__(self, source_string: str, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):

        self.text = remove_not_in_alphabet(
            source_string.upper(), alphabet=alphabet)
        self.length = len(self.text)
        self.map = _create_frequency_map(self.text)

    def print_frequency(self):
        """
        Prints a table in this style: \n
        ```txt
        +--------+--------+-----------+
        | LETTER | COUNTS | FREQUENCY |
        +--------+--------+-----------+
        |      S |      6 |   9.09    |
        |      B |      6 |   9.09    |
        |   .... |   .... | ......... |
        ```
        """

        str_format = "| {0:>6} | {1:>6} | {2:^9.2f} |"
        h_line = "+--------+--------+-----------+"
        print(h_line)
        print("| LETTER | COUNTS | FREQUENCY |")
        print(h_line)

        # prints the list
        for character in self.map:

            # letter count
            count: int = self.map[character]

            # this index freq
            freq: float = round(count / self.length * 100, 2)
            print(str_format.format(character, count, freq))

        print(h_line)

    def crack(self, key_length: int):
        """
        Evaluate the character frequency
        """
        return
