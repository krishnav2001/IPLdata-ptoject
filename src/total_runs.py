import csv

import matplotlib.pyplot as plt

FILE_PATH = "data/deliveries.csv"


def calculate():
    team_runs = {}

    with open(FILE_PATH, newline="", encoding="utf-8") as file:
        deliveries_reader = csv.DictReader(file)

        for delivery in deliveries_reader:
            total_runs = int(delivery["total_runs"])
            team = delivery["batting_team"]

            if team not in team_runs:
                team_runs[team] = 0

            team_runs[team] += total_runs

    return team_runs


def plot(team_runs):
    teams = list(team_runs.keys())
    runs = list(team_runs.values())

    plt.figure(figsize=(14, 7))

    plt.bar(teams, runs, color="skyblue", edgecolor="black")

    plt.title("Total Runs Scored by Each Team in IPL History", fontsize=16)
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")

    plt.xticks(rotation=90)
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.savefig("src/output/total_runs.png")
    plt.show()


def execute():
    team_runs = calculate()
    plot(team_runs)


execute()
