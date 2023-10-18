#!/usr/bin/env python3
from argparse import ArgumentParser
import re

class VigenereCodec:
    def __init__(self, key, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.abc = alphabet
        self.key = key.upper()
        if re.match(f"[^{self.abc}]", self.key):
            raise ValueError("Illegal characters in key")


    def process(self, mode, text):
        text = re.sub(f"[^{self.abc}]", "", text.upper())
        key_len = len(self.key)
        result = ""
        for i in range(len(text)):
            key_value = self.abc.index(self.key[i % key_len])
            text_value = self.abc.index(text[i])
            # choose between (e)ncrypt and (d)ecrypt
            if mode == "e":
                value = (text_value + key_value) % len(self.abc)
                result += self.abc[value]
            else:
                value = (text_value - key_value) % len(self.abc)
                result += self.abc[value]

        return result


def main():
    # parsing arguments
    parser = ArgumentParser(
        prog='Vigenere',
        description='Encrypt and decrypt with the Vigenère cipher')
    parser.add_argument('operation', choices=['e', 'd'])
    parser.add_argument('text', 
        help="Use \" around the text if you want to enter with spaces.")
    parser.add_argument('key')
    args = parser.parse_args()

    # initialise keyword
    vig = VigenereCodec(args.key)
    if args.operation == 'e':
        print(f'Encoded: ', vig.process(args.operation, args.text))
    else:
        print(f'Decoded: ', vig.process(args.operation, args.text))


if __name__ == '__main__':
    main()
