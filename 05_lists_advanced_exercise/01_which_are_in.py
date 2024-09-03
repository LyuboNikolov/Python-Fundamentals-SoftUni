first_sequence = input().split(", ")
second_sequence = input().split(", ")

substrings = []

for first in first_sequence:
    for second in second_sequence:
        if first in second:
            substrings.append(first)
            break

print(substrings)
