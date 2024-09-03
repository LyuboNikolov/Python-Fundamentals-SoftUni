numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    current_smallest = min(numbers)
    numbers.remove(current_smallest)

print(", ".join(str(x) for x in numbers))
