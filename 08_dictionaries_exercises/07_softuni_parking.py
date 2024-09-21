number_commands = int(input())
parked_cars = {}

for n in range(number_commands):
    data = input().split()
    action, name = data[0], data[1]

    if action == "register":
        if name not in parked_cars:
            plate = data[2]
            parked_cars[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parked_cars[name]}")

    elif action == "unregister":
        if name not in parked_cars:
            print(f"ERROR: user {name} not found")
        else:
            del parked_cars[name]
            print(f"{name} unregistered successfully")

[print(f"{key} => {value}") for key, value in parked_cars.items()]
