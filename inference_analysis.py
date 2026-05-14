import csv
import math
from collections import Counter


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

    expected = total_matches / 3
    chi_square = sum(
        (observed - expected) ** 2 / expected
        for observed in [home_wins, draws, away_wins]
    )
    chi_square_df = 2

    # For a chi-square test with df = 2, right-tail p-value = exp(-x / 2).
    chi_square_p_value = math.exp(-chi_square / 2)

    print("Test 1: Chi-square goodness-of-fit test")
    print(f"Expected count for each outcome: {expected:.2f}")
    print(f"Chi-square statistic: {chi_square:.2f}")
    print(f"Degrees of freedom: {chi_square_df}")
    print(f"p-value: {chi_square_p_value:.4e}")
    print()

    non_draw_matches = home_wins + away_wins
    p_hat = home_wins / non_draw_matches
    p0 = 0.50
    standard_error = math.sqrt(p0 * (1 - p0) / non_draw_matches)
    z_score = (p_hat - p0) / standard_error

    # One-tailed p-value: P(Z >= z).
    z_p_value = 0.5 * math.erfc(z_score / math.sqrt(2))

    print("Test 2: One-proportion z-test")
    print(f"Non-draw matches: {non_draw_matches}")
    print(f"Home win proportion among non-draw matches: {p_hat:.4f}")
    print(f"Home win percentage among non-draw matches: {p_hat * 100:.2f}%")
    print(f"z-score: {z_score:.2f}")
    print(f"p-value: {z_p_value:.4e}")


if __name__ == "__main__":
    main()
