# !/usr/bin/python3

from vigenere_cipher import VigenereCipher
from text import TextResource
from character_frequency_analysis import CharacterFrequencyAnalyzer
import sys

assert sys.version_info >= (3, 6, 0), "Python version too low."


if __name__ == "__main__":
    # This README file
    resource = TextResource("./README.md", online_resource=False)

    # Create the VigenereCipher object
    vigenere_cipher = VigenereCipher("newkey", plaintext=resource.text)

    # Setting the text the CharacterFrequencyAnalyzer will use
    analyzer = CharacterFrequencyAnalyzer(vigenere_cipher.plaintext)

    # Print the analysis
    analyzer.print_frequency()

    # Generate a cipher text and use a new cipher analyzer
    cipher_text_analyzer = CharacterFrequencyAnalyzer(
        vigenere_cipher.encrypt())

    # Analysis of the cipher text/encrypted message
    cipher_text_analyzer.print_frequency()
