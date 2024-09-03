lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

total_expenses = 0

for loss in range(1, lost_fights + 1):

    if loss % 2 == 0:
        total_expenses += helmet_price

    if loss % 3 == 0:
        total_expenses += sword_price
        if loss % 2 == 0:
            total_expenses += shield_price
            if loss % 4 == 0:
                total_expenses += armour_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")