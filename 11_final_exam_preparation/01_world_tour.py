def index_is_valid(stops, index):
    return 0 <= index <= len(stops)


def add_stop(stops, index, string):
    if index_is_valid(stops, index):
        stops = stops[:index] + string + stops[index:]
    return stops


def remove_stop(stops, start_index, end_index):
    if index_is_valid(stops, start_index) and index_is_valid(stops, end_index):
        stops = stops[:start_index] + stops[end_index + 1:]
    return stops


def switch(stops, old_string, new_string):
    if old_string in stops:
        stops = stops.replace(old_string, new_string)
    return stops


def print_function(stops):
    print(stops)


def world_tour(stops):
    while True:
        command = input()
        if command == "Travel":
            break

        command_split = command.split(":")
        action = command_split[0]

        if action == "Add Stop":
            index, stop = int(command_split[1]), command_split[2]
            stops = add_stop(stops, index, stop)

        elif action == "Remove Stop":
            start_index, end_index = int(command_split[1]), int(command_split[2])
            if 0 <= start_index <= end_index < len(stops):
                stops = remove_stop(stops, start_index, end_index)

        elif action == "Switch":
            old_string, new_string = command_split[1], command_split[2]
            stops = switch(stops, old_string, new_string)

        print_function(stops)

    print(f"Ready for world tour! Planned stops: {stops}")


data = input()
world_tour(data)
