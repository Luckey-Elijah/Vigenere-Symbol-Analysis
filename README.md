# A Simple Vigenere Cipher and Symbol Analyzer

## Usage

```shell
python3 src/main.py
```

## Using Resources

To access a simple `.txt` resource/file (encoded with UTF-8) use the `TextResource()` class. Set `online_resource=True` if you can access the resource online via a GET request.

```python
# Access an online resource
url = "https://www.gutenberg.org/files/100/100-0.txt"
resource = TextResource(url, online_resource=True)
print(resource.text)
```

Result

```txt
Project Gutenberg’s The Complete Works of William Shakespeare, by William Shakespeare

This eBook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever.  You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this eBook or online at
www.gutenberg.org.  If you are not located in the United States, you’ll
have to check the laws of the country where you are located before using
this ebook.
...
```

Otherwise you can access a local resource by providing the path to it.

```python
resource = TextResource("./README.md")
print(resource.text)
```

Result:

````txt
# A Simple Vigenere Cipher and Symbol Analyzer

## Usage

Run:

```bash
$ python3 main.py
```

## Using Resources

To access a simple `.txt` resource/file (encoded with UTF-8) use the `TextResource()` class. Set `online_resource=True` if you can access the resource online via a GET request.

```python
# Access an online resource
url = "https://www.gutenberg.org/files/100/100-0.txt"
resource = TextResource(url, online_resource=True)
print(resource.text)
```
````

## Encrypt & Decrypt

Use the `VigenereCipher()` class to perform vigenere encryption and decryption with a text.

```python
# This is our plaint text for the example.
text = "Used to perform vigenere encryption. It doesn't retain non-alpha characters."
v = VigenereCipher("newkey", plaintext=text)

# Cipher text is generated with the english alphabet (A-Z).
print("ALPHABET: {}".format(v.alphabet))
print("CIPHER  : {}".format(v.encrypt()))
print("DECRYPT : {}\n".format(v.decrypt()))
```

Result of English alphabet (A-Z):

```txt
ALPHABET: ABCDEFGHIJKLMNOPQRSTUVWXYZ
CIPHER  : NCGTDSIOTVYVFFKWORXBGUXGKIRJSSGSVTYILXVHOXTSPDYRTVRXKGAKTQMXXBU
DECRYPT : USEDTOPERFORMVIGENEREENCRYPTIONITDOESNTRETAINNONALPHACHARACTERS
```

Now with a new `alphabet`.

```python
# A new alphabet is introduced.
v.alphabet = "SUZC7^1NJB%XY35MIE64LO.DVF"

print("ALPHABET: {}".format(v.alphabet))
print("CIPHER  : {}".format(v.encrypt()))
print("DECRYPT : {}".format(v.decrypt()))
```

Result of custom alphabet (`SUZC7^1NJB%XY35MIE64LO.DVF`):

```txt
ALPHABET: SUZC7^1NJB%XY35MIE64LO.DVF
CIPHER  : 3Z14T6P5ROVR^^%G5EDR1LD1RJPT6616T4VJXDTR5TA6MCVEAOPHA1HARAYTDRL
DECRYPT : USEDTOPERFORMVIGENEREENCRYPTIONITDOESNTRETAINNONALPHACHARACTERS
```

## Symbol/Character Analysis

Use the `CharacterFrequencyAnalyzer()` class to perform analysis like below.

In this example we'll bring all parts of the program together.

```python
# This README file
resource = TextResource("./README.md", online_resource=False)

# Create the VigenereCipher object
vigenere_cipher = VigenereCipher("newkey", plaintext=resource.text)

# Setting the text the CharacterFrequencyAnalyzer will use
analyzer = CharacterFrequencyAnalyzer(vigenere_cipher.plaintext)

# Print the analysis
analyzer.print_frequency()
```

Results:

```txt
+--------+--------+-----------+
| LETTER | COUNTS | FREQUENCY |
+--------+--------+-----------+
|      E |    351 |   14.09   |
|      T |    241 |   9.67    |
|      R |    222 |   8.91    |
|      A |    159 |   6.38    |
|      N |    148 |   5.94    |
|      O |    148 |   5.94    |
|      S |    145 |   5.82    |
|      I |    133 |   5.34    |
|      C |    120 |   4.82    |
|      L |     98 |   3.93    |
|      H |     98 |   3.93    |
|      P |     95 |   3.81    |
|      U |     90 |   3.61    |
|      Y |     67 |   2.69    |
|      D |     50 |   2.01    |
|      G |     48 |   1.93    |
|      F |     43 |   1.73    |
|      M |     42 |   1.69    |
|      X |     40 |   1.61    |
|      V |     38 |   1.52    |
|      B |     36 |   1.44    |
|      W |     33 |   1.32    |
|      K |     15 |   0.60    |
|      Z |     14 |   0.56    |
|      J |     10 |   0.40    |
|      Q |      8 |   0.32    |
+--------+--------+-----------+
```

And continuing with a cipher text.

```python
# Generate a cipher text and use a new cipher analyzer
cipher_text_analyzer = CharacterFrequencyAnalyzer(
    vigenere_cipher.encrypt())

# Analysis of the cipher text/encrypted message
cipher_text_analyzer.print_frequency()
```

Results:

```txt
+--------+--------+-----------+
| LETTER | COUNTS | FREQUENCY |
+--------+--------+-----------+
|      X |    167 |   6.70    |
|      B |    139 |   5.58    |
|      I |    137 |   5.50    |
|      O |    133 |   5.34    |
|      V |    132 |   5.30    |
|      K |    130 |   5.22    |
|      E |    126 |   5.06    |
|      M |    116 |   4.65    |
|      G |    112 |   4.49    |
|      U |    105 |   4.21    |
|      D |    102 |   4.09    |
|      C |     97 |   3.89    |
|      Y |     97 |   3.89    |
|      R |     95 |   3.81    |
|      T |     90 |   3.61    |
|      H |     87 |   3.49    |
|      S |     81 |   3.25    |
|      J |     77 |   3.09    |
|      Q |     75 |   3.01    |
|      W |     70 |   2.81    |
|      N |     64 |   2.57    |
|      L |     62 |   2.49    |
|      P |     59 |   2.37    |
|      Z |     57 |   2.29    |
|      F |     48 |   1.93    |
|      A |     34 |   1.36    |
+--------+--------+-----------+
```
