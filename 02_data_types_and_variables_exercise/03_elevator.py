from math import ceil

people = int(input())
elevator_capacity = int(input())

elevator_courses = ceil(people / elevator_capacity)

print(elevator_courses)
