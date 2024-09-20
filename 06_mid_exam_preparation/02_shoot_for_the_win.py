targets = list(map(int, input().split()))
shot_targets = 0

while True:
    command = input()

    if command == "End":
        break

    index = int(command)

    if 0 <= index < len(targets) and targets[index] != -1:
        shot_targets += 1
        special_value = targets[index]
        targets[index] = -1

        for i in range(len(targets)):
            if targets[i] == -1:
                continue
            if special_value < targets[i]:
                targets[i] -= special_value
            else:
                targets[i] += special_value

targets_to_string = [str(x) for x in targets]
print(f"Shot targets: {shot_targets} -> {' '.join(targets_to_string)}")
