electrons = int(input())
shells = []
current_shell = 1

while True:
    result = 2 * (current_shell ** 2)

    if electrons > result:
        electrons -= result
        shells.append(result)

    else:
        shells.append(electrons)
        break
    current_shell += 1

print(shells)
