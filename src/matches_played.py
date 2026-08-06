import csv
import matplotlib.pyplot as plt

DEFAULT_FILE_PATH = "data/matches.csv"


def calculate(file_path):

    print(file_path)
    total_matches_played = {}

    with open(file_path, newline="", encoding="utf-8") as file:
        print("File opened successfully")
        matches = csv.DictReader(file)

        for match in matches:
            print(match)
            season = match["season"]

            team1 = match["team1"]
            team2 = match["team2"]

            if season not in total_matches_played:
                total_matches_played[season] = {}

            if team1 not in total_matches_played[season]:
                total_matches_played[season][team1] = 0

            if team2 not in total_matches_played[season]:
                total_matches_played[season][team2] = 0

            total_matches_played[season][team1] += 1
            total_matches_played[season][team2] += 1

    return total_matches_played


def plot(total_matches_played):

    seasons = sorted(total_matches_played.keys())

    teams = set()

    for season in seasons:
        teams.update(total_matches_played[season].keys())

    teams = sorted(teams)

    bottom = [0] * len(seasons)

    plt.figure(figsize=(14, 7))

    for team in teams:

        matches_played = []

        for season in seasons:
            matches_played.append(
                total_matches_played[season].get(team, 0)
            )

        plt.bar(
            seasons,
            matches_played,
            bottom=bottom,
            label=team
        )

        for i in range(len(bottom)):
            bottom[i] += matches_played[i]

    plt.xlabel("Season")
    plt.ylabel("Matches Played")
    plt.title("Matches Played by Team by Season")

    plt.xticks(rotation=45)

    plt.legend(
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    plt.tight_layout()

    plt.show()


def execute(file_path=DEFAULT_FILE_PATH):

    return calculate(file_path)


if __name__ == "__main__":

    data = execute()

    plot(data)