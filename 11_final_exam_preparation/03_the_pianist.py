number_of_pieces = int(input())
musical_pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    musical_pieces[piece] = [composer, key]

command = input()
while command != "Stop":

    command_split = command.split("|")
    action, piece = command_split[0], command_split[1]

    if action == "Add":
        if piece in musical_pieces:
            print(f"{piece} is already in the collection!")
        else:
            piece_composer, piece_key = command_split[2], command_split[3]
            musical_pieces[piece] = [piece_composer, piece_key]
            print(f"{piece} by {piece_composer} in {piece_key} added to the collection!")

    elif action == "Remove":
        if piece in musical_pieces:
            del musical_pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        new_key = command_split[2]
        if piece in musical_pieces:
            musical_pieces[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

for piece, info in musical_pieces.items():
    print(f"{piece} -> Composer: {info[0]}, Key: {info[1]}")
