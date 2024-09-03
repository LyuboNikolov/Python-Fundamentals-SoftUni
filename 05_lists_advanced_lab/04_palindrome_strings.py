words = input().split()
palindrome = input()

palindromes = [word for word in words if word == word[::-1]]
palindrome_counter = palindromes.count(palindrome)

print(f"{palindromes}\nFound palindrome {palindrome_counter} times")
