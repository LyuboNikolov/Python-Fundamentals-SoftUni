text = input()
chars = {}

for char in text.replace(" ", ""):
    if char not in chars:
        chars[char] = 0
    chars[char] += 1

[print(f"{key} -> {value}") for key, value in chars.items()]
