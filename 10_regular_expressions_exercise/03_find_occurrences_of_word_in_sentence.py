import re

sentence = input()
word = input()
search_pattern = fr"\b{word}\b"
matches = re.findall(search_pattern, sentence, re.IGNORECASE)

print(len(matches))
