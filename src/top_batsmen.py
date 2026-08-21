import csv

import matplotlib.pyplot as plt


def calculate():
    FILE_PATH = "data/deliveries.csv"
    batsman_total_runs = {}

    with open(FILE_PATH, newline="", encoding="utf-8") as file:
        deliveries_reader = csv.DictReader(file)

        for delivery in deliveries_reader:
            if delivery["batting_team"] == "Royal Challengers Bangalore":
                batsman = delivery["batsman"]
                runs = int(delivery["batsman_runs"])

                if batsman not in batsman_total_runs:
                    batsman_total_runs[batsman] = 0

                batsman_total_runs[batsman] += runs

                sorted_batsman_total_runs = sorted(
                    batsman_total_runs.items(), key=lambda x: x[1], reverse=True
                )

                top_10_batsman = dict(sorted_batsman_total_runs[:10])

    return top_10_batsman


def plot(top_10_batsman):
    batsman = list(top_10_batsman.keys())
    batsman_runs = list(top_10_batsman.values())

    plt.figure(figsize=(14, 7))
    plt.xticks(rotation=90)
    plt.bar(batsman, batsman_runs, color="skyblue")
    plt.xlabel("Batsmen")
    plt.ylabel("Total Runs")
    plt.title("Total Runs Scored by Each Batsman in Royal Challengers Bangalore")
    plt.tight_layout()
    plt.savefig("src/output/top_batsmen.png")
    plt.show()


def execute():
    top_10_batsman = calculate()
    plot(top_10_batsman)


execute()
