current_product = input()
current_quantity = int(input())


def calculate_order(product, quantity):
    price = None
    if product == "coffee":
        price = 1.50
    elif product == "coke":
        price = 1.40
    elif product == "water":
        price = 1.00
    elif product == "snacks":
        price = 2.00

    return price * quantity


total_order = calculate_order(current_product, current_quantity)
print(f"{total_order:.2f}")
