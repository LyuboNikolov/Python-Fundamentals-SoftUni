lines = int(input())

COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

numbers = []

for _ in range(lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_numbers = []

for number in numbers:
    filtered_passes = (
        (command == COMMAND_EVEN and number % 2 == 0) or
        (command == COMMAND_ODD and number % 2 != 0) or
        (command == COMMAND_NEGATIVE and number < 0) or
        (command == COMMAND_POSITIVE and number >= 0)
    )

    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)