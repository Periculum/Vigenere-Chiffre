# Vigenère Cipher

Simple Python implementation of the [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

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

### Copyright

Copyright ©️ 2023 Wilhelm Drehling, Heise Medien GmbH & Co. KG

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
