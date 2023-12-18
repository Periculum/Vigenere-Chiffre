from collections import Counter

text = "UIQJPUFNUEHXKDQEBDZEREHQIAZUIQBEDQEUDSBILUTHQELUTHFMEDJUOYTEZEPVNFVXFQUQETLZFRVRZRBQIDQIIZYAXKEDXINKKQZNQESUEN"
letter_frequencies = Counter(text)
index = 0
for n in letter_frequencies.values():
  index += (n/len(text)) * ((n - 1)/(len(text) - 1))
print(index)
