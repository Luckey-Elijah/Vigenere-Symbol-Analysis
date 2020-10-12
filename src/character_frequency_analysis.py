import re
from utils import create_frequency_map, remove_not_in_alphabet


class CharacterFrequencyAnalyzer():
    """
    Used to analyze the characters of a given map, or text based on an alphabet.\n
    Usage:\n
    ```python
    >>> s = "This is the source string ... exclamation mark!"
    >>> x = CharacterFrequencyAnalyzer(s, alphabet="A]{DEFGHI.KLMNO-QRSTUV!XYZ")
    >>> print
    ```
    """

    def __init__(self, text="",  map=None, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ",):

        self.text = remove_not_in_alphabet(
            text.upper(), alphabet=alphabet)

        # evaluating where to determine length of the text

        if type(map) is None:
            __map: dict = {}
            self.map = create_frequency_map(self.text, map=__map, sort=True)
        else:
            self.map = map
        __length = len(self.text)
        if __length < 1 and map is not None:
            # case to use map
            self.length = 0
            for count in self.map.values():
                self.length = self.length + count
        elif map is None:
            self.length = __length
        else:
            raise AssertionError()

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
            count: int = self.map[character]

            # this index freq
            freq: float = round(count / self.length * 100, 2)
            print(str_format.format(character, count, freq))

        print(h_line)
