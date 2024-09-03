wagons = int(input())
train = [0] * wagons

command = input()

while command != "End":

    split_command = command.split()
    action = split_command[0]

    if action == "add":
        people_to_add = int(split_command[1])
        train[-1] += people_to_add

    elif action == "insert":
        index = int(split_command[1])
        people_to_insert = int(split_command[2])
        train[index] += people_to_insert

    elif action == "leave":
        index = int(split_command[1])
        people_to_remove = int(split_command[2])
        train[index] -= people_to_remove

    command = input()

print(train)