group_size = int(input())
days = int(input())

companions = group_size
total_coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        companions -= 2

    if day % 15 == 0:
        companions += 5

    total_coins += 50 - 2 * companions

    if day % 3 == 0:
        total_coins -= 3 * companions

    if day % 5 == 0:
        total_coins += 20 * companions
        if day % 3 == 0:
            total_coins -= 2 * companions

coins_per_companion = int(total_coins / companions)

print(f"{companions} companions received {coins_per_companion} coins each.")
