tickets_cost = 150
items = input().split("|")
budget = float(input())

profit = 0
bought_items_price = []

for item in items:
    current_item = item.split("->")
    item_type = current_item[0]
    item_price = float(current_item[1])

    if (item_type == "Clothes" and item_price <= 50) or \
            (item_type == "Shoes" and item_price <= 35) or \
            (item_type == "Accessories" and item_price <= 20.50):
        if item_price <= budget:
            budget -= item_price
            bought_items_price.append(item_price)

for price in bought_items_price:
    profit += price * 0.4
    sell_price = price * 1.4
    budget += sell_price
    print(f"{sell_price:.2f}", end=" ")

print(f'\nProfit: {profit:.2f}')

if budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
