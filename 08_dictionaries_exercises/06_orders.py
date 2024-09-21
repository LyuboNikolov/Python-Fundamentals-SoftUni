command = input()
products = {}
prices = {}

while command != "buy":
    name, price, quantity = command.split()
    if name not in products:
        products[name] = int(quantity)
    else:
        products[name] += int(quantity)
    prices[name] = float(price)

    command = input()

for product in products:
    products[product] *= prices[product]

[print(f"{key} -> {value:.2f}") for key, value in products.items()]
