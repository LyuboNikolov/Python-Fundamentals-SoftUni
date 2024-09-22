command = input()
force_sides = {}

while command != "Lumpawaroo":

    if "|" in command:
        side, user = command.split(" | ")

        user_exists = any(user in users for users in force_sides.values())

        if not user_exists:
            force_sides[side] = force_sides.get(side, [])
            force_sides[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")

        if side not in force_sides:
            force_sides[side] = []

        for force in force_sides.values():
            if user in force:
                force.remove(user)
                break

        force_sides[side].append(user)
        print(f"{user} joins the {side} side!")

    command = input()

for side, users in force_sides.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        [print(f"! {user}") for user in users]
