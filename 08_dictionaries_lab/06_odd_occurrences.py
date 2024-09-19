words = input().lower().split()
words_counter = {}

for word in words:
    if word not in words_counter:
        words_counter[word] = 0
    words_counter[word] += 1

for key, value in words_counter.items():
    if value % 2 != 0:
        print(key, end=" ")
