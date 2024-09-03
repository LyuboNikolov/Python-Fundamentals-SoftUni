text = input()
vowels = ["a", "o", "u", "e", "i"]

new_text = [char for char in text if char.lower() not in vowels]
print(*new_text, sep="") #"".join(new_text)
