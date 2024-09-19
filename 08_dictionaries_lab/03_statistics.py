command = input()
products = {}

while command != "statistics":
    product, quantity = command.split(": ")
    if product not in products:
        products[product] = 0
    products[product] += int(quantity)

    command = input()

print(f"Products in stock:")
[print(f"- {product}: {quantity}") for product, quantity in products.items()]
print(f"Total Products: {len(products)}\nTotal Quantity: {sum(products.values())}")
