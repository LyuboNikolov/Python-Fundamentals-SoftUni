number_students = int(input())
grades = {}

for _ in range(number_students):
    name, grade = input(), float(input())
    grades[name] = grades.get(name, [])
    grades[name].append(grade)

for student, values in grades.items():
    average = sum(values) / len(values)
    if average >= 4.50:
        print(f"{student} -> {average:.2f}")
