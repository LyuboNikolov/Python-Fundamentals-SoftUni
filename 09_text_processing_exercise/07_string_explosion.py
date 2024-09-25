string = input()
new_string = ""
strength = 0

for index in range(len(string)):
    if strength > 0 and string[index] != ">":
        strength -= 1
    elif string[index] == ">":
        new_string += ">"
        strength += int(string[index + 1])
    else:
        new_string += string[index]

print(new_string)
