def factorial_division(first_num, second_num):
    first_result = first_num
    second_result = second_num

    for num in range(1, first_num):
        first_result *= num

    for num in range(1, second_num):
        second_result *= num

    return f"{(first_result / second_result):.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))
