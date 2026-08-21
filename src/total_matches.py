import csv

import matplotlib.pyplot as plt


def calculate():
    FILE_PATH = "data/matches.csv"
    total_matches = {}

    with open(FILE_PATH, newline="", encoding="utf-8") as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            season = match["season"]

            if season not in total_matches:
                total_matches[season] = 0

            total_matches[season] += 1

    return total_matches


def plot(total_matches):
    seasons = sorted(list(total_matches.keys()))
    matches = list(total_matches.values())

    plt.figure(figsize=(14, 7))
    plt.xticks(rotation=90)
    plt.bar(seasons, matches, color="skyblue")
    plt.xlabel("Seasons")
    plt.ylabel("Total Matches")
    plt.title("Number of matches played per year for all the years in IPL")
    plt.tight_layout()
    plt.savefig("src/output/total_matches.png")
    plt.show()


def execute():
    total_matches = calculate()
    plot(total_matches)


execute()
