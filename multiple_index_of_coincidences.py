from collections import Counter, defaultdict

def calculate_single_index(group):
    return sum((n / len(group)) * ((n - 1) / (len(group) - 1))
                for n in Counter(group).values())
  
def calculate_avg_index(text, key_length):
    groups = [""] * key_length
    for i, char in enumerate(text):
        groups[i % key_length] += char
    total = sum(calculate_single_index(group)
                for group in groups)
    return total / key_length

text = "UIQJPUFNUEHXKDQEBDZEREHQIAZUIQBEDQEUDSBILUTHQELUTHFMEDJUOYTEZEPVNFVXFQUQETLZFRVRZRBQIDQIIZYAXKEDXINKKQZNQESUEN".upper()
min_key_length, max_key_length = 2, 10
for key_length in range(min_key_length, max_key_length + 1):
    average_index = calculate_avg_index(text, key_length)
    print(f"""The index of coincidence for the key length {key_length:2d} is {average_index:.4f}""")
