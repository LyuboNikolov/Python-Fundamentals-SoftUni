def loading_number(number):
    if number == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    else:
        result = (number // 10) * "%" + (10 - (number // 10)) * "."
        return f"{number}% [{result}]\nStill loading..."


integer_number = int(input())
print(loading_number(integer_number))
