factor = int(input())
count = int(input())

list_of_multiples = []

for number in range(1, count + 1):
    current_number = number * factor
    list_of_multiples.append(current_number)

print(list_of_multiples)