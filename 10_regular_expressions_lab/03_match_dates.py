import re

dates = input()
search_pattern = r"\b([0-9]{2})(\/|-|.)([A-Z]{1}[a-z]{2})\2(\d{4})"
matches = re.findall(search_pattern, dates)

for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
