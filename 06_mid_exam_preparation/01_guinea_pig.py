food_quantity = float(input())
hay_quantity = float(input())
cover_quantity = float(input())
guineas_weight = float(input())

for day in range(1, 31):
    food_quantity -= 0.3

    if day % 2 == 0:
        hay_quantity -= 0.05 * food_quantity

    if day % 3 == 0:
        cover_quantity -= guineas_weight / 3

    if round(food_quantity) <= 0 or round(hay_quantity) <= 0 or round(cover_quantity) <= 0:
        print("Merry must go to the pet store!")
        break

else:
    print(f"Everything is fine! Puppy is happy! "
          f"Food: {food_quantity:.2f}, Hay: {hay_quantity:.2f}, Cover: {cover_quantity:.2f}.")
