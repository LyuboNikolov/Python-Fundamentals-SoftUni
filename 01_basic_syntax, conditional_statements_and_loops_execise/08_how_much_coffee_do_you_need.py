command = input()
coffees_needed = 0

while command != "END":

    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffees_needed += 1
    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffees_needed += 2

    command = input()

if coffees_needed <= 5:
    print(coffees_needed)
else:
    print("You need extra sleep")
