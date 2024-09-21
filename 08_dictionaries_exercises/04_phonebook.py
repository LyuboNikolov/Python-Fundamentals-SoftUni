command = input()
phonebook = {}

while "-" in command:
    name, number = command.split("-")
    phonebook[name] = number

    command = input()

contacts = int(command)

for name in range(contacts):
    current_name = input()
    if current_name in phonebook:
        print(f"{current_name} -> {phonebook[current_name]}")
    else:
        print(f"Contact {current_name} does not exist.")
