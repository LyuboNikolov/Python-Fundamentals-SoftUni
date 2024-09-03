message_sent = int(input())

for num in range(message_sent):
    current_num = int(input())
    if current_num == 88:
        print("Hello")
    elif current_num == 86:
        print("How are you?")
    elif current_num > 88:
        print("Bye.")
    else:
        print("GREAT!")
