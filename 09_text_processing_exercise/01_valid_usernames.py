def length_is_valid(name):
    if not 3 <= len(name) <= 16:
        return False
    return True


def characters_are_valid(name):
    for char in name:
        if not char.isalnum() and char != "-" and char != "_":
            return False
    return True


def no_redundant_symbols(name):
    if " " in name:
        return False
    return True


usernames = input().split(", ")
for username in usernames:
    if length_is_valid(username) and characters_are_valid(username) and no_redundant_symbols(username):
        print(username)
