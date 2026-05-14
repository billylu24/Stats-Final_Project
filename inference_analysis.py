import csv
import math
from collections import Counter


def chi_square_p_value_df2(chi_square):
    """Right-tail p-value for a chi-square distribution with 2 degrees of freedom."""
    return math.exp(-chi_square / 2)


def main():
    with open("epl_final.csv", newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))

    counts = Counter(row["FullTimeResult"] for row in rows)

    home_wins = counts["H"]
    draws = counts["D"]
    away_wins = counts["A"]
    total_matches = home_wins + draws + away_wins

    print("Observed match outcomes")
    print(f"Home wins: {home_wins}")
    print(f"Draws: {draws}")
    print(f"Away wins: {away_wins}")
    print(f"Total matches: {total_matches}")
    print()

    expected_each = total_matches / 3
    gof_chi_square = sum(
        (observed - expected_each) ** 2 / expected_each
        for observed in [home_wins, draws, away_wins]
    )
    gof_df = 2
    gof_p_value = chi_square_p_value_df2(gof_chi_square)

    print("Test 1: Chi-square goodness-of-fit test")
    print(f"Expected count for each outcome: {expected_each:.2f}")
    print(f"Chi-square statistic: {gof_chi_square:.2f}")
    print(f"Degrees of freedom: {gof_df}")
    print(f"p-value: {gof_p_value:.4e}")
    print()

    observed_table = {
        "Home": {"Win": home_wins, "Draw": draws, "Loss": away_wins},
        "Away": {"Win": away_wins, "Draw": draws, "Loss": home_wins},
    }

    venues = ["Home", "Away"]
    outcomes = ["Win", "Draw", "Loss"]
    row_totals = {
        venue: sum(observed_table[venue][outcome] for outcome in outcomes)
        for venue in venues
    }
    column_totals = {
        outcome: sum(observed_table[venue][outcome] for venue in venues)
        for outcome in outcomes
    }
    grand_total = sum(row_totals.values())

    independence_chi_square = 0
    expected_table = {}
    for venue in venues:
        expected_table[venue] = {}
        for outcome in outcomes:
            expected = row_totals[venue] * column_totals[outcome] / grand_total
            expected_table[venue][outcome] = expected
            observed = observed_table[venue][outcome]
            independence_chi_square += (observed - expected) ** 2 / expected

    independence_df = (len(venues) - 1) * (len(outcomes) - 1)
    independence_p_value = chi_square_p_value_df2(independence_chi_square)

    print("Test 2: Chi-square test for independence")
    print("Observed table")
    print("Venue, Win, Draw, Loss")
    for venue in venues:
        print(
            f"{venue}, "
            f"{observed_table[venue]['Win']}, "
            f"{observed_table[venue]['Draw']}, "
            f"{observed_table[venue]['Loss']}"
        )
    print("Expected table")
    print("Venue, Win, Draw, Loss")
    for venue in venues:
        print(
            f"{venue}, "
            f"{expected_table[venue]['Win']:.2f}, "
            f"{expected_table[venue]['Draw']:.2f}, "
            f"{expected_table[venue]['Loss']:.2f}"
        )
    print(f"Chi-square statistic: {independence_chi_square:.2f}")
    print(f"Degrees of freedom: {independence_df}")
    print(f"p-value: {independence_p_value:.4e}")


if __name__ == "__main__":
    main()
