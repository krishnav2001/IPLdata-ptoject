import csv
import matplotlib.pyplot as plt

def calculate(file_path="data/matches.csv"):
    matches_won = {}

    with open(file_path, newline="", encoding="utf-8") as file:
        matches = csv.DictReader(file)

        for match in matches:
            season = match["season"]
            winner = match["winner"]

            if season not in matches_won:
                matches_won[season] = {}

            if winner not in matches_won[season]:
                matches_won[season][winner] = 0

            matches_won[season][winner] += 1

    return matches_won


def plot(matches_won):
    seasons = sorted(matches_won.keys())
    teams = set()

    for season in seasons:
        teams.update(matches_won[season].keys())

    teams = sorted(teams)

    bottom = [0] * len(seasons)

    plt.figure(figsize=(14, 7))

    for team in teams:
        wins = []

        for season in seasons:
            wins.append(matches_won[season].get(team, 0))

        plt.bar(seasons, wins, bottom=bottom, label=team)

        for i in range(len(bottom)):
            bottom[i] += wins[i]

    plt.xticks(rotation=90)
    plt.xlabel("Season")
    plt.ylabel("Matches Won")
    plt.title("Matches Won Per Team Per Year")

    plt.legend()

    plt.tight_layout()

    plt.show()


def execute(file_path="data/matches.csv"):
    """Return the matches won per season mapping.

    This function is test-friendly and returns the computed dict; it does not plot.
    """
    return calculate(file_path)

