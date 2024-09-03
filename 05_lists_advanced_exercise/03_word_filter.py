even_length = [word for word in input().split() if len(word) % 2 == 0]
print(*even_length, sep="\n")
