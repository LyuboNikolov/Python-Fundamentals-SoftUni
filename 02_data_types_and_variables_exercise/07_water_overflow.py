water_tank_capacity = 255
pours = int(input())
tank_fullness = 0

for pour in range(pours):
    current_pour = int(input())

    if tank_fullness + current_pour <= water_tank_capacity:
        tank_fullness += current_pour
    else:
        print(f"Insufficient capacity!")

print(tank_fullness)
