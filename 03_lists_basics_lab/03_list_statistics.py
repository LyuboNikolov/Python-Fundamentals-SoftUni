numbers = int(input())

positive_numbers = []
negative_numbers = []

for _ in range(numbers):
    current_number = int(input())

    if current_number >= 0:
        positive_numbers.append(current_number)
    else:
        negative_numbers.append(current_number)

print(f"{positive_numbers}\n{negative_numbers}\n"
      f"Count of positives: {len(positive_numbers)}\n"
      f"Sum of negatives: {sum(negative_numbers)}")
