number_of_letters = int(input())
start_index = ord("a")
end_index = start_index + number_of_letters

for first_letter in range(start_index, end_index):
    for second_letter in range(start_index, end_index):
        for third_letter in range(start_index, end_index):
            print(f"{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}")
