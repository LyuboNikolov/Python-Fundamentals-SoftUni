import re

text = input()
destinations = []
travel_points = 0

search_pattern = r"(=|\/)([A-Z][A-Za-z]{2,})(\1)"
matches = re.findall(search_pattern, text)

for match in matches:
    destination = match[1]
    destinations.append(destination)
    travel_points += len(destination)

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")
