import csv
import matplotlib.pyplot as plt

def calculate(deliveries_path="data/deliveries.csv", matches_path="data/matches.csv"):
    total_extra_runs = {}
    match_ids = set()

    with open(matches_path, newline="", encoding="utf-8") as file:
        matches = csv.DictReader(file)

        for match in matches:
            if match["season"] == "2016":
                match_ids.add(match["id"])

    with open(deliveries_path, newline="", encoding="utf-8") as file:
        deliveries = csv.DictReader(file)

        for delivery in deliveries:
            if delivery["match_id"] in match_ids:
                team = delivery["bowling_team"]
                extra_runs = int(delivery["extra_runs"])

                if team not in total_extra_runs:
                    total_extra_runs[team] = 0

                total_extra_runs[team] += extra_runs

    return total_extra_runs


def plot(total_extra_runs):
    teams = list(total_extra_runs.keys())
    extra_runs = list(total_extra_runs.values())

    plt.figure(figsize=(14, 7))
    plt.xticks(rotation=90)
    plt.bar(teams, extra_runs, color="skyblue")
    plt.xlabel("Teams")
    plt.ylabel("Total Extra Runs")
    plt.title("Total Extra Runs Conceded by Each Team in 2016 IPL Season")
    plt.tight_layout()
    plt.show()


def execute(deliveries_path="data/deliveries.csv", matches_path="data/matches.csv"):
    """Return the total extra runs conceded per team for 2016.

    The function returns a dict mapping bowling_team to total extra runs.
    """
    return calculate(deliveries_path, matches_path)