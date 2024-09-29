import re

sentence = input()
search_pattern = r"\b_([A-Za-z0-9]+)\b"
matches = re.findall(search_pattern, sentence)
print(",".join(matches))
