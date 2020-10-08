# !/usr/bin/python3
from character_frequency_analysis import CharacterFrequencyAnalyzer
from vigenere_cipher import VigenereCipher, VigenereCracker
from text import TextResource
import sys

assert sys.version_info >= (3, 6, 0), "Python version too low."


if __name__ == "__main__":
    # the plaintext
    t = TextResource(
        "https://www.gutenberg.org/files/100/100-0.txt", online_resource=True)

    # key
    k = "WORDS"

    # the ciphertext: v.encrypt()
    v = VigenereCipher(k, plaintext=t.text)

    # cracking the cipher
    c = VigenereCracker(cipher_text=v.encrypt())
