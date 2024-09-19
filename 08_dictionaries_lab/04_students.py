students = {}
command = input()

while ":" in command:
    name, student_id, course_name = command.split(":")
    students[name, student_id] = course_name

    command = input()

searched_course = command.replace("_", " ")

for student, course in students.items():
    if searched_course == course:
        print(f"{student[0]} - {student[1]}")
