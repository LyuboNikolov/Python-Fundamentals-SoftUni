def character_multiplier(first_str, second_str):
    total_sum = 0
    min_length = min(len(first_str), len(second_str))

    for index in range(min_length):
        total_sum += ord(first_str[index]) * ord(second_str[index])

    if len(first_str) > len(second_str):
        for index in range(len(second_str), len(first_str)):
            total_sum += ord(first_str[index])
    elif len(second_str) > len(first_str):
        for index in range(len(first_str), len(second_str)):
            total_sum += ord(second_str[index])

    return total_sum


first_string, second_string = input().split()
result = (character_multiplier(first_string, second_string))
print(result)
