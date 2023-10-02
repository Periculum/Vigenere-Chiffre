# Vigenere-Chiffre
Simple [Vigenere-Chiffre](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) with on keyword and an implementation of the Kasiski-Test to find the length of the keyword (ToDo).

### Usage

You will need python to execute the Code.
There are a total of three parameters that the program can take. d/e for decode or encode, followed by the text and the keyword (the keyword must be uppercase!) Note: The program removes all spaces from the text and turns it into one with only uppercase letters.
```
python3 vigenere.py <d/e> <text> <keyword>
```

### Encrypting

If you want to encrypt the text "Lorem ipsum dolor sit" with the keywords "CTMAGAZIN", the command would look like this:
```
python3 vigenere.py e "Lorem ipsum dolor sit" CTMAGAZIN
```

It will return NHDESIOAHOWALURRQG.

### Decrypting

If you want to decrypt the message NHDESIOAHOWALURRQG:
```
python3 vigenere.py d NHDESIOAHOWALURRQG CTMAGAZIN
```

The output is LOREMIPSUMDOLORSIT.

### Copyright

Copyright ©️ 2023 Wilhelm Drehling, Heise Medien GmbH & Co. KG

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see https://www.gnu.org/licenses/.
