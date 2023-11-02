#!/usr/bin/env python3
from argparse import ArgumentParser
import re

class KasiskiTest:
    def __init__(self, text, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.text = re.sub(f"[^{alphabet}]", "", text.upper())


    def find_distance_between_sequences(self):
        #create sequences of the length upwards of 3
        sequences = {}
        for i in range(len(self.text)):
            for j in range(3, len(self.text) - i + 1):
                seq = self.text[i:i + j]
                if seq in sequences:
                    sequences[seq].append(i)
                else:
                    sequences[seq] = [i]

        # sort all seqs out that appear just one time (key > 1)
        sequences_cleaned = {}
        for seq, value in sequences.items():
            if len(value) > 1:
                sequences_cleaned[seq] = value

        # calculate distance
        distances = []
        for seq, positions in sequences_cleaned.items():
            for i in range(len(positions) - 1):
                distances.append((positions[i] - positions[i + 1]) * (-1))

        return distances


    def get_primefactors(self, number):
        i = 2
        while i * i <= number:
            while number % i == 0:
                number //= i
                yield i
            i += 1
        if number > 1:
            yield number


    def get_candidate_key_length(self, distances):
        # calculate for all distances primfactors and put them in one list
        prime_factors = []
        for num in distances:
            prime_factors.extend(self.get_primefactors(num))

        # Find the numbers with the highest frequency
        frequency = {}
        for num in range(len(prime_factors)):
            buffer = prime_factors[num]
            if buffer in frequency:
                frequency[buffer] += 1
            else:
                frequency[buffer] = 1

        # sort frequency
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return sorted_frequency

    def attack(self):
        distances = self.find_distance_between_sequences()
        candidate_key_length = self.get_candidate_key_length(distances)

        for number, freq in candidate_key_length:
            print(f"The factor {number} appeared {freq} times")

        if len(candidate_key_length) >= 2:
            print(f"The Keylength is most likely {candidate_key_length[0][0]}, {candidate_key_length[1][0]} or a product of that.")
        else:
            print(f"The Keylength is most likely {candidate_key_length[0][0]} or a product of that.")


def main():
    # parsing arguments
    parser = ArgumentParser(
        prog='Kasiski-Attack',
        description='Find candidate key length for long Vigenere ciphers')
    parser.add_argument('cipher',
        help="Use \" around the text if you want to enter with spaces.")
    args = parser.parse_args()

    kasiski = KasiskiTest(args.cipher)
    kasiski.attack()


if __name__ == '__main__':
    main()
