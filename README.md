# Vigenère Cipher

Simple Python implementation of the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).
An article on this cipher appeared in the german c't-magazin 25/2023 p.154. An online version can be found on [heise online](https://www.heise.de/select/ct/2023/25/2327113243167325005).

## Prerequisites

- Python 3
 
## Usage

There are a total of three parameters the program can take. d/e for decode or encode, followed by the text and the keyword:

```
python3 vigenere.py <d/e> <text> <keyword>
```

Note: The program removes all spaces and other characters from the text and turns it into one with only uppercase letters:

Windows users: On Windows you don't need to write `python3 ...`, `python ...` is enough.

### Encrypting

To encrypt the text `Lorem ipsum dolor sit` with the keyword `CTMAGAZIN`, simply type:

```
python3 vigenere.py e "Lorem ipsum dolor sit" CTMAGAZIN
```

This will return `NHDESIOAHOWALURRQG`.

### Decrypting

To decrypt the message `NHDESIOAHOWALURRQG` type:

```
python3 vigenere.py d NHDESIOAHOWALURRQG CTMAGAZIN
```

The output is `LOREMIPSUMDOLORSIT`.

### Modification

You can modify the program to decrypt and encrypt whatever you like. You just need to remove ```.upper()``` from the line ```text = re.sub(f"[^{self.abc}]", "", text.upper())``` and add letters to ```alphabet``` like that:
```
alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789,. '"
```
Now you can use more chars like shown in this example:
```
python3 vigenere.py e "Die c't ist dieses Jahr 40 geworden." CTMAGAZIN
Encoded:  F1q i'EGvu KdoeDm5Acmhx P8Lix8oxd3vK

python3 vigenere.py d "F1q i'EGvu KdoeDm5Acmhx P8Lix8oxd3vK" CTMAGAZIN
Decoded:  Die c't ist dieses Jahr 40 geworden.
```

# Kasiksi-Test

```kasiski.py``` contains a simple implementation of the [Kasiksi-Examination](https://en.wikipedia.org/wiki/Kasiski_examination).

## Usage

By default, the Kasiski test only outputs the prime factors that are already sorted by frequency. You can insert the text directly on the command line (cipher) or read it from a file (-f FILE). If you also want to get an initial assessment using a simple frequency analysis, use -a.

```
python3 kasiski.py <-a> <cipher> [-f FILE]
```
Note: The analyse function works best with german texts. If the text is in another language, you must replace the letter (```shift = (self.abc.index(letter) - self.abc.index("E")) % len(self.abc)```) in the frequency analysis with the letter that appears most frequently in the other language.
Windows users: On Windows you don't need to write `python3 ...`, `python ...` is enough.

Example: If you want to obtain the factors for a cipher and then analyse possible key lengths, the command looks like this:

```
python3 kasiski.py -a GNVSYEIYLRLBNZQQXRUGYAQDYAUFNJMIWUMJGNVFGTMEYVUBHPWOLRAMIALFYEMKQVTIZHMODRLBHOCZBFBXVRVBCAMYYFWKXRZBWUQCZEMRHQAZBEMFVGLXHAUFNQQBMRVZBVNCLRVFHQMOARELYUVICPPBHNZQ
Factor 2 appeared 23 times
Factor 3 appeared 5 times
Factor 5 appeared 1 times
Factor 29 appeared 1 times
The key length is most likely 2, 3 or a product of that.
Which key length do you want to test? (Format: 3 5 15)2 4 6 8
Possible Key: IN
Possible Key: UNIX
Possible Key: INRBHN
Possible Key: CNIBUMMX
```

The key is UNIX. You can then decode the cipher with vigenère.py. 

### Copyright

Copyright ©️ 2023 Wilhelm Drehling, Heise Medien GmbH & Co. KG

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
