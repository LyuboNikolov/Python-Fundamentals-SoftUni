def min_max_sum(numbers):
    return f"The minimum number is {min(numbers)}\n" \
           f"The maximum number is {max(numbers)}\n" \
           f"The sum number is: {sum(numbers)}"


list_of_integers = [int(x) for x in input().split()]
print(min_max_sum(list_of_integers))
