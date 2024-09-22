command = input()
users = {}
submissions = {}

while command != "exam finished":

    if "banned" not in command:
        name, language, points = command.split("-")
        points = int(points)

        if name not in users:
            users[name] = {language: points}
        else:
            current_points = users[name].get(language, 0)
            if points > current_points:
                users[name].update({language: points})

        submissions[language] = submissions.get(language, 0) + 1

    else:
        name, banned = command.split("-")
        del users[name]

    command = input()

print(f"Results:")
for user, languages in users.items():
    for score in languages.values():
        print(f"{user} | {score}")

print(f"Submissions:")
[print(f"{language} - {count}") for language, count in submissions.items()]
