def palindrome_integers(numbers):
    for num in numbers:
        if num == num[::-1]:
            print(True)
        else:
            print(False)

list_of_integers = input().split(", ")
palindrome_integers(list_of_integers)