decorations_quantity = int(input())
days_left_to_christmas = int(input())

money_spent = 0
christmas_spirit = 0

ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

for day in range(1, days_left_to_christmas + 1):

    if day % 11 == 0:
        decorations_quantity += 2

    if day % 2 == 0:
        money_spent += ornament_price * decorations_quantity
        christmas_spirit += 5

    if day % 3 == 0:
        money_spent += (tree_skirt_price + tree_garland_price) * decorations_quantity
        christmas_spirit += 13

    if day % 5 == 0:
        money_spent += tree_lights_price * decorations_quantity
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30

    if day % 10 == 0:
        christmas_spirit -= 20
        money_spent += tree_garland_price + tree_skirt_price + tree_lights_price

if days_left_to_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")
