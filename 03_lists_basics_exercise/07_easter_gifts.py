gifts = input().split()
command = input()

while command != "No Money":
    data = command.split()
    action = data[0]
    current_gift = data[1]

    if action == "OutOfStock":
        for gift in range(len(gifts)):
            if gifts[gift] == current_gift:
                gifts[gift] = None

    elif action == "Required":
        for gift in range(len(gifts)):
            if gift == int(data[2]):
                gifts[gift] = current_gift

    elif action == "JustInCase":
        gifts[-1] = current_gift

    command = input()

result = " ".join(x for x in gifts if x is not None)
print(result)
