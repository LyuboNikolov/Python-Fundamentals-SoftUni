numbers = [int(x) for x in input().split(", ")]  # list(map(int, input().split(", "))
indices = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

# for index in range(len(numbers)):
#     if numbers[index] % 2 == 0:
#         indices.append(index)

print(indices)
