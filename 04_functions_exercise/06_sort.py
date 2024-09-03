def sort_numbers(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers


list_of_integers = [int(x) for x in input().split()]
print(sort_numbers(list_of_integers))
