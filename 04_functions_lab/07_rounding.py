sequence_of_numbers = input().split()


def rounding(numbers):
    result = [round(float(x)) for x in numbers]
    return result


print(rounding(sequence_of_numbers))
