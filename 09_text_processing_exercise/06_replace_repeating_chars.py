string = input()
new_string = ""
last_letter = ""

for current_letter in string:
    if current_letter != last_letter:
        new_string += current_letter
        last_letter = current_letter

print(new_string)
