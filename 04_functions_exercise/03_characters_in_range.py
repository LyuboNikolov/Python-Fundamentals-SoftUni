def characters_in_range(first, second):
    ascii_characters = []
    for number in range(ord(first) + 1, ord(second)):
        ascii_characters.append(chr(number))

    return ascii_characters


first_character = input()
second_character = input()
print(*(characters_in_range(first_character, second_character)))
