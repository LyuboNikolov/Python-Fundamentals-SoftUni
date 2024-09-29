import re

bought_furniture = []
total_money = 0
search_pattern = r">>([A-Za-z]+)<<(\d+\.?\d*)+!(\d+)"
command = input()

while command != "Purchase":
    match = re.search(search_pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        bought_furniture.append(furniture)
        total_money += float(price) * int(quantity)
    command = input()

print(f"Bought furniture:")
for furniture in bought_furniture:
    print(furniture)
print(f"Total money spend: {total_money:.2f}")
