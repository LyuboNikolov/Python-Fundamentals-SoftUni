def perfect_number(number_to_check):
    total_sum = 0
    for divisor in range(1, (number_to_check // 2) + 1):
        if number_to_check % divisor == 0:
            total_sum += divisor

    if total_sum == number_to_check:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_number(number))
