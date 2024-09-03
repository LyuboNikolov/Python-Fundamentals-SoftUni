deck_of_cards = input().split()
shuffles = int(input())

new_deck = deck_of_cards
middle_of_deck = len(deck_of_cards) // 2


while shuffles > 0:
    left_part = new_deck[:middle_of_deck]
    right_part = new_deck[middle_of_deck:]
    new_deck = []
    for card in range(middle_of_deck):
        new_deck.append(left_part[card])
        new_deck.append(right_part[card])
    shuffles -= 1

print(new_deck)