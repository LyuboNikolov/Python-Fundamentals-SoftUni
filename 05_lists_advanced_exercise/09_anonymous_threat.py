# message = input().split()
#
# command = input()
#
# while command != "3:1":
#
#     split_command = command.split()
#     action = split_command[0]
#
#     if action == "merge":
#         start_index, end_index = int(split_command[1]), int(split_command[2])
#         if start_index < 0:
#             start_index = 0
#         elif end_index >= len(message):
#             end_index = len(message) - 1
#         merged = "".join(message[start_index:end_index + 1])
#         message = message[:start_index] + [merged] + message[end_index + 1:]
#
#     elif action == "divide":
#         index, partitions = int(split_command[1]), int(split_command[2])
#         original_string = message[index]
#
#         part_length = len(original_string) // partitions
#         remainder = len(original_string) % partitions
#
#         divided = []
#         start = 0
#
#         for i in range(partitions):
#             part_size = part_length + 1 if i < remainder else part_length
#             divided.append(original_string[start:start + part_size])
#             start += part_size
#
#         message = message[:index] + divided + message[index + 1:]
#
#     command = input()
#
# print(" ".join(message))

def merge(list_name, start_index, end_index):
    if start_index < 0:
        start_index = 0
    result_list = list_name[:start_index]
    merged_element = ""
    index_is_in_range = True
    if end_index >= len(list_name):
        end_index = len(list_name) - 1
        index_is_in_range = False
    for index in range((end_index + 1) - start_index):
        current_index = index + start_index
        merged_element += list_name[current_index]
    result_list.append(merged_element)
    if index_is_in_range:
        result_list += list_name[(end_index + 1):]
    return result_list


def divide(list_name, index, partitions):
    result_list = list_name[:index]
    string_to_divide = list_name[index]
    current_substring = ""
    last_substring = ""
    letters_in_partition = len(string_to_divide) // partitions
    if len(string_to_divide) % partitions != 0:
        slice_index = (partitions - 1) * letters_in_partition
        last_substring = string_to_divide[slice_index:]
        string_to_divide = string_to_divide[:slice_index]
    for letter in string_to_divide:
        current_substring += letter
        if len(current_substring) == letters_in_partition:
            result_list.append(current_substring)
            current_substring = ""
    if last_substring != "":
        result_list.append(last_substring)
    if (index + 1) < len(list_name):
        result_list += list_name[index + 1:]
    return result_list


data_array = input().split()
command = input()
while command != "3:1":
    current_command = command.split()[0]
    first_value = int(command.split()[1])
    second_value = int(command.split()[2])
    if current_command == "merge":
        data_array = merge(data_array, first_value, second_value)
    elif current_command == "divide":
        data_array = divide(data_array, first_value, second_value)
    command = input()
print(" ".join(data_array))