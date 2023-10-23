def team_lineup(*args):
    team_information = {}

    for player, country in args:
        if country not in team_information:
            team_information[country] = []
        if player not in team_information[country]:
            team_information[country].append(player)

    sorted_team = dict(sorted(team_information.items(), key=lambda x: (-len(x[1]), x[0])))
    final_result = []
    for country, players in sorted_team.items():
        final_result.append(f"{country}:")
        for player in players:
            final_result.append(f"  -{player}")
    return '\n'.join(final_result)


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))

print('==========')

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

print('==========')

print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))
