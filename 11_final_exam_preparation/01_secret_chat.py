message = input()
real_message = message

while message != "Reveal":

    command = message.split(":|:")
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        real_message = real_message[:index] + " " + real_message[index:]
        print(real_message)

    elif action == "Reverse":
        substring = command[1]
        if substring in real_message:
            start_index = real_message.index(substring)
            end_index = start_index + len(substring)
            real_message = real_message[:start_index] + real_message[end_index:] + substring[::-1]
            print(real_message)
        else:
            print("error")

    elif action == "ChangeAll":
        substring_to_remove, replacement = command[1], command[2]
        real_message = real_message.replace(substring_to_remove, replacement)
        print(real_message)

    message = input()

print(f"You have a new text message: {real_message}")
