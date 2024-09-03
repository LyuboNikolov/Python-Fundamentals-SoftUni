budget = float(input())
price_one_kg_flour = float(input())
eggs_price = 0.75 * price_one_kg_flour
milk_250_ml = (1.25 * price_one_kg_flour) * 0.25

loaves = 0
bread_cost = price_one_kg_flour + eggs_price + milk_250_ml
coloured_eggs = 0

while budget >= bread_cost:

    budget -= bread_cost
    loaves += 1
    coloured_eggs += 3

    if loaves % 3 == 0:
        coloured_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {coloured_eggs} eggs and {budget:.2f}BGN left.")
