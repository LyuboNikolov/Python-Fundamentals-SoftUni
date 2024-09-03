rooms = int(input())
free_chairs = 0
needed_chairs = 0
sufficient_chairs = True

for room in range(1, rooms + 1):
    room_info = input().split()
    chairs = room_info[0].count("X")
    people = int(room_info[1])

    if people <= chairs:
        free_chairs += chairs - people
        continue

    needed_chairs = people - chairs
    sufficient_chairs = False
    print(f"{needed_chairs} more chairs needed in room {room}")

if sufficient_chairs:
    print(f"Game On, {free_chairs} free chairs left")
