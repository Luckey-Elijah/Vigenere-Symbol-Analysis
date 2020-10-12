# !/usr/bin/python3
from character_frequency_analysis import CharacterFrequencyAnalyzer
from vigenere_cipher import VigenereCipher, VigenereCracker
from text import TextResource
import sys

assert sys.version_info >= (3, 6, 0), "Python version too low."


if __name__ == "__main__":
    # the plaintext
    t = TextResource("example_literature/shakespeare.txt")

    # key
    k = "AB"

    # the ciphertext: v.encrypt()
    v = VigenereCipher(k, plaintext=t.text, )

    # cracking the cipher
    c = VigenereCracker(cipher_text=v.encrypt())

    # set up the
    assumed_key_len = 2
    maps = c.crack_one_length(assumed_key_len)

    for i in range(assumed_key_len):
        analyzer = CharacterFrequencyAnalyzer(map=maps[i])
        analyzer.print_frequency()
