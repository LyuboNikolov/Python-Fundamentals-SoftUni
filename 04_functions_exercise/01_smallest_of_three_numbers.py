def smallest_of_three_numbers(first_num, second_num, third_num):
    all_nums = [first_num, second_num, third_num]
    return min(all_nums)


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = smallest_of_three_numbers(first_number, second_number, third_number)
print(result)
