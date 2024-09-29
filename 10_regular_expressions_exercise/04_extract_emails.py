import re

sentence = input()
search_pattern = r"\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b"
matches = re.findall(search_pattern, sentence)

for match in matches:
    print(match[0])
