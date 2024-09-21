key_materials = {"shards": 0, "fragments": 0, "motes": 0}
items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
junk_materials = {}
win_points = 250
item_is_found = False

while not item_is_found:
    materials = input().split()
    for i in range(1, len(materials) + 1, 2):
        current_material, current_quantity = materials[i].lower(), materials[i - 1]
        if current_material in key_materials:
            key_materials[current_material] += int(current_quantity)

            if key_materials[current_material] >= win_points:
                print(f"{items[current_material]} obtained!")
                key_materials[current_material] -= win_points
                item_is_found = True
                break
        else:
            junk_materials[current_material] = junk_materials.get(current_material, 0)
            junk_materials[current_material] += int(current_quantity)

[print(f"{key}: {value}") for key, value in key_materials.items()]
[print(f"{key}: {value}") for key, value in junk_materials.items()]
