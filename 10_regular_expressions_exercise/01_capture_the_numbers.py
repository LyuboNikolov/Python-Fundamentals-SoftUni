import re

line = input()
search_pattern = r"\d+"

while line:
    matches = re.findall(search_pattern, line)
    if matches:
        print(*matches, end=" ")

    line = input()
