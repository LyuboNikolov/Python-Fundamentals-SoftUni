string = input()

for index in range(len(string)):
    if string[index] == ":":
        print(f":{string[index + 1]}")
