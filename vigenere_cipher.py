import sys


def _assert_char_key_alphabet(char, key, alphabet) -> None:
    # Assert char and key are the characters
    if len(char) > 1 or len(key) > 1 or len(alphabet) != 26:
        print("Please provide a single character. You provided:")
        print("char: {}".format(char))
        print("key:  {}".format(key))
        raise AssertionError()
    elif type(char) is not str or type(key) is not str or type(alphabet) is not str:
        print("Not the correct type.")
        raise TypeError()


def _encrypt_letter(char, key, alphabet) -> str:
    """
    Encrypt an individual letter with a given `char`, `key`, and `alphabet`.
    ```txt
    E = (P + K) mod 26
    ```
    """

    _assert_char_key_alphabet(char, key, alphabet)

    if char not in alphabet:
        return char

    p = ord(char) - 65  # plaintext value
    k = ord(key) - 65   # key value
    e = (p + k) % 26    # encrypted value

    enc_char = alphabet[e]
    return enc_char


def _decrypt_letter(char, key, alphabet) -> str:
    """
    Decrypt an individual letter with a given `char`, `key`, and `alphabet`.
    ```txt
    P = (E - K + 26) mod 26
    ```
    """

    _assert_char_key_alphabet(char, key, alphabet)

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
    Removes non-alphabetic characters (including whitespace). [`a-zA-Z`].
    """
    # Assert text
    if len(text) < 1 or type(text) is not str:
        raise AssertionError()

    trimmed_text = ""
    for letter in text:
        if letter in alphabet:
            trimmed_text = trimmed_text + letter

    return trimmed_text


class VigenereCipher():
    """
    Used to perform vigenere encryption, vigenere decryption, and analysis on text.
    `key` must be type `str`. Only use plaintext or cipher text. They will be written over.\n
    ```python
    v = VigenereCipher("key", plaintext="")
    ```
    """

    def __init__(self, key, plaintext=None, cipher_text=None, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        # Assert key given.
        if (type(key) is not str):
            print("Key type: {}".format(type(key)))
            raise TypeError()
        elif (len(key) < 3):
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
            plntxt_char = plaintext[char_index]

            # encrypts the single letter
            ciph_char = _encrypt_letter(plntxt_char, key_char, self.alphabet)

            # Append to the new *encrypted* letter to the cipher.
            cipher_text = cipher_text + ciph_char

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
            ciph_txt_char = ciphertext[char_index]

            # decrypt the current index key
            plntxt_char = _decrypt_letter(
                ciph_txt_char, key_char, self.alphabet)

            # append it to the plain text
            plaintext_str = plaintext_str + plntxt_char

        if update_plaintext is True:
            self.plaintext = plaintext_str

        return plaintext_str
