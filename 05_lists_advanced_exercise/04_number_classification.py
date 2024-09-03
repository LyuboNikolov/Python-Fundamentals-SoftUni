numbers = [int(num) for num in input().split(", ")]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 != 0]

print(f"Positive: {', '.join(str(num) for num in positive_nums)}\n"
      f"Negative: {', '.join(str(num) for num in negative_nums)}\n"
      f"Even: {', '.join(str(num) for num in even_nums)}\n"
      f"Odd: {', '.join(str(num) for num in odd_nums)}")
