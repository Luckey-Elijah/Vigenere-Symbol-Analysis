# A Simple Vigenere Cipher and Symbol Analyzer

## Usage

```bash
# install requirements
pip3 install -r requirements.txt

# run
python3 src/main.py
```

## Using Resources

To access a simple `.txt` resource/file (encoded with UTF-8) use the `TextResource()` class.
Set `online_resource=True` if you can access the resource online via a GET request.

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

..

.
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

```shell
python3 src/main.py
```

## Using Resources

To access a simple `.txt` resource/file (encoded with UTF-8) use the `TextResource()` class.
Set `online_resource=True` if you can access the resource online via a GET request.

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

In this example we'll bring parts of the program together.

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

## Cipher Cracking Utility

Use the `VigenereCracker()` object to perform additional analysis directly to cipher text.

Use the `VigenereCracker().crack_one_length()` method to perform analysis on the ciphertext for an assumed length.

```python

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
```

Results:

```txt
+--------+--------+-----------+
| LETTER | COUNTS | FREQUENCY |
+--------+--------+-----------+
|      E | 239822 |   11.90   |
|      T | 176307 |   8.75    |
|      O | 165672 |   8.22    |
|      A | 154561 |   7.67    |
|      I | 134275 |   6.67    |
|      S | 133180 |   6.61    |
|      N | 130023 |   6.45    |
|      H | 127745 |   6.34    |
|      R | 125528 |   6.23    |
|      L |  90390 |   4.49    |
|      D |  78967 |   3.92    |
|      U |  68466 |   3.40    |
|      M |  58548 |   2.91    |
|      Y |  49530 |   2.46    |
|      W |  47760 |   2.37    |
|      C |  45639 |   2.27    |
|      F |  42932 |   2.13    |
|      G |  36312 |   1.80    |
|      B |  31795 |   1.58    |
|      P |  30513 |   1.51    |
|      V |  20074 |   1.00    |
|      K |  18631 |   0.92    |
|      X |   2678 |   0.13    |
|      J |   2401 |   0.12    |
|      Q |   1946 |   0.10    |
|      Z |    873 |   0.04    |
+--------+--------+-----------+
+--------+--------+-----------+
| LETTER | COUNTS | FREQUENCY |
+--------+--------+-----------+
|      F | 240066 |   11.92   |
|      U | 176346 |   8.75    |
|      P | 165827 |   8.23    |
|      B | 154383 |   7.66    |
|      J | 134014 |   6.65    |
|      T | 132848 |   6.59    |
|      O | 129573 |   6.43    |
|      I | 127459 |   6.33    |
|      S | 125347 |   6.22    |
|      M |  89935 |   4.46    |
|      E |  79341 |   3.94    |
|      V |  68459 |   3.40    |
|      N |  58728 |   2.92    |
|      Z |  49631 |   2.46    |
|      X |  48203 |   2.39    |
|      D |  45743 |   2.27    |
|      G |  42843 |   2.13    |
|      H |  36102 |   1.79    |
|      C |  31998 |   1.59    |
|      Q |  30638 |   1.52    |
|      W |  20049 |   1.00    |
|      L |  19023 |   0.94    |
|      Y |   2657 |   0.13    |
|      K |   2422 |   0.12    |
|      R |   1997 |   0.10    |
|      A |    936 |   0.05    |
+--------+--------+-----------+
```
