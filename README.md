# EPL Home-Field Advantage Inference Project

Names: Billy Lu, Jaewan Lim  
Period: ___  
Project type: Traditional

## Topic

We are investigating home-field advantage in English Premier League matches. We want to see whether playing at home affects the final result of a match.

The data file is `epl_final.csv`. The main column we use is `FullTimeResult`:

- `H` = home team won
- `D` = draw
- `A` = away team won

Observed match results:

| Result | Count |
|---|---:|
| Home wins | 4,299 |
| Draws | 2,313 |
| Away wins | 2,768 |
| Total matches | 9,380 |

## Inference Question 1

### Test

Chi-square goodness-of-fit test

### Question

Is the distribution of English Premier League match outcomes different from what would be expected if home-field advantage did not exist?

### Hypotheses

`H0`: Home wins, draws, and away wins are equally likely.  
`Ha`: Home wins, draws, and away wins are not equally likely.

### Process

Under the null hypothesis, each outcome would have the same expected count:

```text
9380 / 3 = 3126.67
```

| Outcome | Observed | Expected |
|---|---:|---:|
| Home win | 4,299 | 3,126.67 |
| Draw | 2,313 | 3,126.67 |
| Away win | 2,768 | 3,126.67 |

### Result

Chi-square statistic: `692.45`  
Degrees of freedom: `2`  
p-value: about `4.33 x 10^-151`

### Conclusion

Because the p-value is much smaller than `0.05`, we reject the null hypothesis. EPL match outcomes are not equally distributed, and home wins happen more often than expected under an equal distribution.

## Inference Question 2

### Test

Chi-square test for independence

### Question

Is the result of a game independent of the venue?

This test checks whether there is a statistical link between two categorical variables:

- Venue: Home or Away
- Outcome: Win, Draw, or Loss

### Hypotheses

`H0`: Venue and outcome are independent.  
`Ha`: Venue and outcome are not independent.

### Process

Each match is counted from both team perspectives:

- If the home team wins, the home team gets `Win` and the away team gets `Loss`.
- If the away team wins, the away team gets `Win` and the home team gets `Loss`.
- If the match is a draw, both teams get `Draw`.

Observed two-way table:

| Venue | Win | Draw | Loss | Total |
|---|---:|---:|---:|---:|
| Home | 4,299 | 2,313 | 2,768 | 9,380 |
| Away | 2,768 | 2,313 | 4,299 | 9,380 |
| Total | 7,067 | 4,626 | 7,067 | 18,760 |

Expected counts if venue and outcome are independent:

| Venue | Win | Draw | Loss |
|---|---:|---:|---:|
| Home | 3,533.50 | 2,313.00 | 3,533.50 |
| Away | 3,533.50 | 2,313.00 | 3,533.50 |

### Result

Chi-square statistic: `663.35`  
Degrees of freedom: `2`  
p-value: about `9.01 x 10^-145`

### Conclusion

Because the p-value is much smaller than `0.05`, we reject the null hypothesis. There is strong evidence that match outcome is related to venue. Home teams are more likely to win, while away teams are more likely to lose.

## Other Possible Tests

Matched pairs t-test: Compare the difference in points earned at home vs. away for every team in a specific season. This would work best with a complete season. Our current dataset does not include the full 2025-2026 season.

One-proportion z-test: Remove draws and test whether the home win proportion among non-draw matches is greater than `0.50`.

## Overall Conclusion

Both main inference tests support the idea that home-field advantage exists in English Premier League matches. The data shows that home wins are more common than away wins, and the relationship between venue and outcome is statistically significant.

## Python Pseudocode

```text
load epl_final.csv
count H, D, and A in the FullTimeResult column

for chi-square goodness-of-fit:
    expected count = total matches / 3
    compare observed H, D, A counts to expected counts
    calculate chi-square statistic and p-value

for chi-square test for independence:
    create a two-way table:
        Home venue: Win = H, Draw = D, Loss = A
        Away venue: Win = A, Draw = D, Loss = H
    calculate row totals, column totals, and expected counts
    calculate chi-square statistic and p-value

print the results
```

To reproduce the results, run:

```powershell
python inference_analysis.py
```
