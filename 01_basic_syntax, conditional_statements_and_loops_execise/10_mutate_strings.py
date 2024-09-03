first_string = input()
second_string = input()

current_string = first_string

for letter in range(len(current_string)):

    if current_string[letter] != second_string[letter]:
        left_part = second_string[:letter + 1]
        right_part = first_string[letter + 1:]
        new_string = left_part + right_part
        current_sting = new_string

        print(new_string)
