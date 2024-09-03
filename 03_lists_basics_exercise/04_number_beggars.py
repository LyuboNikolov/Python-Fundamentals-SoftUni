money = input().split(", ")
beggars = int(input())
copy_beggars = beggars

final_sums = []
index = 0

while copy_beggars > 0:
    sum_current_beggar = 0
    for offer in range(index, len(money), beggars):
        sum_current_beggar += int(money[offer])
    final_sums.append(sum_current_beggar)
    copy_beggars -= 1
    index += 1

print(final_sums)
