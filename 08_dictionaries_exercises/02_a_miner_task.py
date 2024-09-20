resource = input()
resources = {}

while resource != "stop":
    amount = int(input())
    if resource not in resources:
        resources[resource] = 0
    resources[resource] += amount

    resource = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
