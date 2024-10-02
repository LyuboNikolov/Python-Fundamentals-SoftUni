import re

word = input()
search_pattern = r"(@|#)([A-za-z]{3,})(\1{2})([A-Za-z]{3,})(\1)"
pairs_found = re.findall(search_pattern, word)
mirror_words = []

if pairs_found:
    print(f"{len(pairs_found)} word pairs found!")
else:
    print("No word pairs found!")
    print("No mirror words!")
    exit()

for word in pairs_found:
    if word[1][::-1] == word[3]:
        mirror_words.append(f"{word[1]} <=> {word[3]}")

if mirror_words:
    mirror_words_joined = ", ".join(mirror_words)
    print(f"The mirror words are:\n{mirror_words_joined}")
else:
    print("No mirror words!")
