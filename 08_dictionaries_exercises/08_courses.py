command = input()
courses = {}

while command != "end":
    course_name, student_name = command.split(" : ")

    courses[course_name] = courses.get(course_name, [])
    courses[course_name].append(student_name)

    command = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}\n" + '\n'.join([f"-- {s}" for s in students]))
