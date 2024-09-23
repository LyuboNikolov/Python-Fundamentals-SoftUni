string = input()
digits, letters, others = "", "", ""

for symbol in string:
    if symbol.isdigit():
        digits += symbol
    elif symbol.isalpha():
        letters += symbol
    else:
        others += symbol

print(f"{digits}\n{letters}\n{others}")
