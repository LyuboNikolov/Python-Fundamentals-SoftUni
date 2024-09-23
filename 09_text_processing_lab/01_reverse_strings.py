while True:

    text = input()

    if text == "end":
        break

    reversed_text = text[::-1]
    print(f"{text} = {reversed_text}")
