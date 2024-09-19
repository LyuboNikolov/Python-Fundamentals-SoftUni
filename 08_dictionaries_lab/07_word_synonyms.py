words = int(input())

synonyms = {}

for word in range(words):
    current_word, synonym = input(), input()

    if current_word not in synonyms:
        synonyms[current_word] = []
    synonyms[current_word].append(synonym)

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
