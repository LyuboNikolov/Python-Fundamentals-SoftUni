word = input()
reverse_word = ""

for char in range(len(word) - 1, -1, -1):
    reverse_word += word[char]

print(reverse_word)
# print(word[::-1])
