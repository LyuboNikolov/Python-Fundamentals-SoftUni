def sum_numbers(first_num, second_num):
    return first_num + second_num


def subtract(result, third):
    return result - third


def add_and_subtract(first, second, third):
    sum_first_and_second = sum_numbers(first, second)
    return subtract(sum_first_and_second, third)


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(add_and_subtract(first_number, second_number, third_number))
