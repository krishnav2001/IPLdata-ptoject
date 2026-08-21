import csv

import matplotlib.pyplot as plt


def calculate(deliveries_path="data/deliveries.csv", matches_path="data/matches.csv"):
    economy = {}
    match_ids = set()
    bowler_runs = {}
    bowler_balls = {}

    with open(matches_path, newline="", encoding="utf-8") as file:
        matches_reader = csv.DictReader(file)

        for match in matches_reader:
            if match["season"] == "2015":
                match_ids.add(match["id"])

    with open(deliveries_path, newline="", encoding="utf-8") as file:
        deliveries_reader = csv.DictReader(file)

        for delivery in deliveries_reader:
            if delivery["match_id"] in match_ids:
                bowler = delivery["bowler"]
                runs = int(delivery["total_runs"])

                if bowler not in bowler_runs:
                    bowler_runs[bowler] = 0
                    bowler_balls[bowler] = 0

                if delivery["wide_runs"] == "0" and delivery["noball_runs"] == "0":
                    bowler_balls[bowler] += 1

                bowler_runs[bowler] += runs

    for bowler in bowler_runs:
        # guard against division by zero (should not occur with reasonable data)
        balls = bowler_balls.get(bowler, 0)
        if balls == 0:
            # skip bowlers with zero legal deliveries
            continue
        economy[bowler] = bowler_runs[bowler] / (balls / 6)

    sorted_economy = sorted(economy.items(), key=lambda x: x[1])
    top_10_economy = dict(sorted_economy[:10])

    return top_10_economy


def plot(top_10_economy):
    bowlers = list(top_10_economy.keys())
    economy_rates = sorted(list(top_10_economy.values()))

    plt.figure(figsize=(14, 7))
    plt.xticks(rotation=90)
    plt.bar(bowlers, economy_rates, color="skyblue")
    plt.xlabel("Bowlers")
    plt.ylabel("Economy Rate")
    plt.title("Economy Rate of Bowlers in 2015 IPL Season")
    plt.tight_layout()
    plt.savefig("src/output/top_economy.png")
    plt.show()


def execute(deliveries_path="data/deliveries.csv", matches_path="data/matches.csv"):
    """Return the top economical bowlers (mapping bowler->economy) for 2015.

    The returned dict contains up to top 10 bowlers sorted by economy ascending.
    """
    return calculate(deliveries_path, matches_path)


if __name__ == "__main__":
    data = execute()
    plot(data)
