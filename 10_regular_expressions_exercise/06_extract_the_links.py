import re

valid_urls = []
search_pattern = r"(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
line = input()

while line:
    matches = re.search(search_pattern, line)
    if matches:
        valid_urls.append(matches.group(0))

    line = input()

for valid_url in valid_urls:
    print(valid_url)
