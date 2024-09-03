def even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


list_of_integers = [int(x) for x in input().split()]
print(even_numbers(list_of_integers))
