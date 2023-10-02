#!/usr/bin/env python3
import string
from argparse import ArgumentParser

class Vigenere:
    def __init__(self, key, text):
        self.alphabet = list(string.ascii_uppercase)
        self.key = key
        self.text = text


    def use_Vigenere(self, mode):
        result = ''
        for i in range(len(self.text)):
            key_value = self.alphabet.index(self.key[i % len(self.key)])
            text_value = self.alphabet.index(self.text[i])
            # choose between (e)ncrypt and (d)ecrypt
            if mode == 'e':
                value = (text_value + key_value) % len(self.alphabet)
                result += self.alphabet[value]
            else:
                value = (text_value - key_value) % len(self.alphabet)
                result += self.alphabet[value]

        return result


def main():
    # parsing arguments
    parser = ArgumentParser(prog='Vigenere', description='Encrypting and Decrypting with the Vigenere Chiffre')
    parser.add_argument('operation', choices=['e', 'd'])
    parser.add_argument('text', help="Use \" around the text if you want to enter with spaces.")
    parser.add_argument('key')
    args = parser.parse_args()

    # remove all spaces and use just upper case
    text = args.text.upper().replace(" ","")

    # initialise keyword and text
    vig = Vigenere(args.key, text)
    if args.operation == 'e':
        print(f'Plain Text: ', vig.use_Vigenere(args.operation))
    else:
        print(f'Chiffre: ', vig.use_Vigenere(args.operation))


if __name__ == '__main__':
    main()
