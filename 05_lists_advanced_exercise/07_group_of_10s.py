from math import ceil

sequence = [int(x) for x in input().split(", ")]
max_group = ceil(max(sequence) / 10) * 10

group_boundary = 0

for group in range(group_boundary, max_group, 10):
    group_list = [num for num in sequence if group_boundary < num <= (group_boundary + 10)]
    group_boundary += 10
    print(f"Group of {group_boundary}'s: {group_list}")
    group_list.clear()
