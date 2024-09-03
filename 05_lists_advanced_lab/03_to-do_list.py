tasks = []

command = input()

while command != "End":
    notes = command.split("-")
    importance = int(notes[0])
    note = notes[1]

    tasks.append((importance, note))

    command = input()

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
