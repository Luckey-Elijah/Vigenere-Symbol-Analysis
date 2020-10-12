import sys
import character_frequency_analysis as cfa
import utils as utils
from text import TextResource
from utils import assert_char_key_alphabet, encrypt_letter, decrypt_letter, remove_not_in_alphabet


class VigenereCipher():
    """
    Used to perform vigenere encryption, vigenere decryption, and analysis on text.
    `key` must be type `str`. Only use plaintext or cipher text. They will be written over.\n
    ```python
    v = VigenereCipher("key", plaintext="")
    ```
    """

    def __init__(self, key: str, plaintext=None, cipher_text=None, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        # Assert key given.
        if (type(key) is not str):
            print("Key type: {}".format(type(key)))
            raise TypeError()
        elif (len(key) < 0):
            raise AssertionError()
        else:
            self.key = key

        # If init with values, assert and create them.

        # plaintext
        if plaintext and type(plaintext) is not str:
            # When plaintext is given check its type
            raise TypeError()
        else:
            self.plaintext = plaintext

        # cipher_text
        if cipher_text and type(cipher_text) is not str:
            # When cipher_text is given check its type
            raise TypeError()
        else:
            self.cipher_text = cipher_text

        # alphabet
        if type(alphabet) is not str:
            # When alphabet is given check its type
            raise TypeError()
        elif len(alphabet) != 26:
            # When alphabet is given check its length
            raise AssertionError()
        else:
            self.alphabet = alphabet

    def _gen_full_key(self) -> str:
        """
        Generates the full-length key give the `key` and `plaintext` cipher.
        """
        # doesn't generate by len(self.cipher_text)
        if self.plaintext and len(self.key) == len(self.plaintext):
            return self.key
        elif self.cipher_text and len(self.key) == len(self.cipher_text):
            return self.key

        key = self.key

        if self.plaintext is not None:
            for letter in range(len(self.plaintext) - len(self.key)):
                key = key + key[letter % len(key)]
            return key
        elif self.cipher_text is not None:
            for letter in range(len(self.cipher_text) - len(self.key)):
                key = key + key[letter % len(key)]
            return key
        else:
            raise AssertionError()

    def encrypt(self, update_cipher_text=True) -> str:
        """
        Encrypts the `self.plaintext` field and returns the cipher text. Set `update_cipher=True` to update this (`self.cipher_text`) instance.
        """

        cipher_text = ""
        full_key = self._gen_full_key()
        plaintext = remove_not_in_alphabet(self.plaintext.upper())

        for char_index in range(len(plaintext)):

            # obtain just the letter of this iteration
            key_char = full_key[char_index]
            plaintext_char = plaintext[char_index]

            # encrypts the single letter
            cipher_char = encrypt_letter(
                plaintext_char, key_char, self.alphabet)

            # Append to the new *encrypted* letter to the cipher.
            cipher_text = cipher_text + cipher_char

        if update_cipher_text is True:
            self.cipher_text = cipher_text

        return cipher_text

    def decrypt(self, update_plaintext=False) -> str:
        """
        Function that returns `str` of the decrypted ciphertext.
        """

        # Assert cipher text
        if self.cipher_text is None:
            raise AssertionError()

        plaintext_str = ""
        full_key = self._gen_full_key()
        ciphertext = self.cipher_text.upper()

        for char_index in range(len(ciphertext)):
            key_char = full_key[char_index]
            cipher_txt_char = ciphertext[char_index]

            # decrypt the current index key
            plaintext_char = decrypt_letter(
                cipher_txt_char, key_char, self.alphabet)

            # append it to the plain text
            plaintext_str = plaintext_str + plaintext_char

        if update_plaintext is True:
            self.plaintext = plaintext_str

        return plaintext_str


class VigenereCracker():
    """
    Used to estimate a key and plain text of a given cipher text.
    If you omit the `symbol_frequencies` dictionary, a new one will be generated.
    If you omit the `word_list_path` value, it will fetch an online word list.
    """

    def __init__(self, cipher_text: str, word_list_path=None, symbol_frequencies=None):
        self.cipher_text = cipher_text

        if symbol_frequencies is None or type(symbol_frequencies) is not dict:
            __map: dict = {}
            self.map = cfa.create_frequency_map(cipher_text, __map)

        if word_list_path is None or type(word_list_path) is not str:
            self.word_list_path = TextResource(
                "http://www.mieliestronk.com/corncob_caps.txt", online_resource=True)

    def crack_one_length(self, key_length: int) -> list:
        # TODO: crack the password?
        """
        Attempts to crack `self.cipher_text` assuming length is the provided `key_length`.
        """

        list_o_maps: list = []

        if key_length < 1:
            raise AssertionError()

        for mod in range(key_length):
            map: dict = {}
            for index in range(len(self.cipher_text)):
                if index % key_length == mod:
                    map = utils.create_frequency_map(
                        self.cipher_text[index], map, sort=True)
            list_o_maps.append(map)

        return list_o_maps
