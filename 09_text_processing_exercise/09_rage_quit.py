data = input()
message, current_word, current_number = "", "", ""
characters, numbers = [], []

for index in range(0, len(data)):
    if not data[index].isnumeric():
        current_word += data[index]
        if current_number:
            numbers.append(current_number)
            current_number = ""
    else:
        if current_word:
            characters.append(current_word)
            current_word = ""
        current_number += data[index]

if current_word:
    characters.append(current_word)
if current_number:
    numbers.append(current_number)

for index in range(len(characters)):
    message += characters[index].upper() * int(numbers[index])

unique_symbols = len(set(message))
print(f"Unique symbols used: {unique_symbols}\n{message}")
