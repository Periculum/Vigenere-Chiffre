#!/usr/bin/env python3
from argparse import ArgumentParser
import re

class KasiskiTest:
    def __init__(self, text, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        self.text = re.sub(f"[^{alphabet}]", "", text.upper())
        self.abc = alphabet


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
                distances.append((positions[i + 1] - positions[i]))

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
            prime_factor = prime_factors[num]
            frequency[prime_factor] = frequency.get(prime_factor, 0) + 1          

        # sort frequency
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return sorted_frequency


    def find_most_used_char(self, row, keylength):
        # analyse frequency of chars in text
        frequency = {}
        for num in range(row, len(self.text), keylength):
            fragment = self.text[num]
            frequency[fragment] = frequency.get(fragment, 0) + 1

        # sort frequency to get the char that appears the most
        sorted_frequency = sorted(frequency.items(), key=lambda item: item[1], reverse=True)
        return sorted_frequency[0][0]


    def find_key(self, keylength):
    	# construct possible key
    	key = ""
    	for element in range(keylength):
    		letter = self.find_most_used_char(element, keylength)
    		# decode
    		shift = (self.abc.index(letter) - self.abc.index("E")) % len(self.abc)
    		key += self.abc[shift]

    	return key


    def attack(self):
        distances = self.find_distance_between_sequences()
        candidate_key_length = self.get_candidate_key_length(distances)

        for number, freq in candidate_key_length:
            print(f"Factor {number} appeared {freq} times")

        if len(candidate_key_length) >= 2:
            print(f"The key length is most likely {candidate_key_length[0][0]}, {candidate_key_length[1][0]} or a product of that.")
        elif len(candidate_key_length) == 1:
            print(f"The key length is most likely {candidate_key_length[0][0]} or a product of that.")
        else:
            print(f"No matching sequences found.")

        return candidate_key_length


    def decode(self):
    	user_input = input("Which key length do you want to test? (Format: 3 5 15)")
    	for n in [int(n) for n in user_input.split()]:
    		print(f"Possible Key: {self.find_key(n)}")


def main():
    # parsing arguments
    parser = ArgumentParser(
        prog='Kasiski-Attack',
        description='Find possible key lengths for long Vigenere ciphers')
    parser.add_argument('-a', '--analyse', required=False, action="store_true",
        help="Evaluates key lengths and outputs a possible key for the length")
    parser.add_argument('-f', '--file', required=False,
                        help="file containing the cipher text")
    parser.add_argument('cipher', nargs='?',
        help="Use \" around the text if you want to enter with spaces.")
    args = parser.parse_args()

    if args.file:
        with open(args.file, 'r') as file:
            cipher = file.read()
    else:
        cipher = args.cipher

    kasiski = KasiskiTest(cipher)
    candidate_key_length = kasiski.attack()
    if args.analyse:
        kasiski.decode()


if __name__ == '__main__':
    main()
