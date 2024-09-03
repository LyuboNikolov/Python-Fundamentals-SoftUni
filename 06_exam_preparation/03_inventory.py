collecting_items = input().split(", ")

command = input()
while command != "Craft!":
    action, item = command.split(" - ")

    if action == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)

    elif action == "Drop":
        if item in collecting_items:
            collecting_items.remove(item)

    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in collecting_items:
            old_item_index = collecting_items.index(old_item)
            collecting_items.insert(old_item_index + 1, new_item)

    elif action == "Renew":
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)

    command = input()

print(", ".join(collecting_items))
