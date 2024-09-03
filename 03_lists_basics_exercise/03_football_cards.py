team_a = ["A-" + str(p) for p in range(1, 12)]
team_b = ["B-" + str(p) for p in range(1, 12)]

players_sent_off = input().split()
games_is_terminated = False

for player in players_sent_off:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)

    if len(team_a) < 7 or len(team_b) < 7:
        games_is_terminated = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if games_is_terminated:
    print(f"Game was terminated")