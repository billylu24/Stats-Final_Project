# EPL Home-Field Advantage Inference Project

Names: Billy Lu, Jaewan Lim  
Period: ___  
Project type: Traditional

## Topic

We are investigating home-field advantage in English Premier League matches. Our question is whether home teams perform better than away teams using real EPL match data from `epl_final.csv`.

The dataset contains match results from 2000 to 2025. For this project, we mainly use the `FullTimeResult` column:

- `H` = home win
- `D` = draw
- `A` = away win

Observed results:

| Result | Count |
|---|---:|
| Home wins | 4,299 |
| Draws | 2,313 |
| Away wins | 2,768 |
| Total | 9,380 |

## Inference Question 1: Are match outcomes equally distributed?

### Test

Chi-square goodness-of-fit test

### Question

Is the distribution of EPL match outcomes different from what would be expected if home-field advantage did not exist?

### Hypotheses

`H0`: Home wins, draws, and away wins are equally likely.  
`Ha`: Home wins, draws, and away wins are not equally likely.

### Conditions

- The data is categorical.
- There are three outcome groups: home win, draw, away win.
- The expected count for each group is large enough.
- Expected count for each group: `9380 / 3 = 3126.67`

### Results

| Result | Observed | Expected |
|---|---:|---:|
| Home wins | 4,299 | 3,126.67 |
| Draws | 2,313 | 3,126.67 |
| Away wins | 2,768 | 3,126.67 |

Chi-square statistic: `692.45`  
Degrees of freedom: `2`  
p-value: about `4.33 x 10^-151`

### Conclusion

Because the p-value is much smaller than `0.05`, we reject the null hypothesis. There is strong evidence that EPL match outcomes are not equally distributed. Home wins happen much more often than expected under an equal distribution.

## Inference Question 2: Do home teams win more often than away teams?

### Test

One-proportion z-test

### Question

After removing draws, is the home win rate higher than the away win rate?

### Hypotheses

`H0: p = 0.50`  
`Ha: p > 0.50`

Here, `p` is the proportion of home wins among non-draw matches.

### Conditions

- We only use matches that ended with a winner.
- There are 7,067 non-draw matches.
- Home wins: 4,299
- Away wins: 2,768
- The success/failure counts are both greater than 10.

### Results

Sample proportion:

```text
p-hat = 4299 / 7067 = 0.6083
```

This means home teams won about `60.83%` of non-draw matches.

z-score: `18.21`  
p-value: about `2.07 x 10^-74`

### Conclusion

Because the p-value is much smaller than `0.05`, we reject the null hypothesis. There is strong evidence that home teams win more often than away teams when draws are removed.

## Overall Conclusion

Both inference tests support the idea that home-field advantage exists in English Premier League matches. Home teams won more often than away teams, and the difference is statistically significant.

## Python Pseudocode

```text
load epl_final.csv
count how many rows have FullTimeResult = H, D, and A

for chi-square test:
    total matches = H + D + A
    expected count = total matches / 3
    calculate chi-square statistic
    calculate p-value

for one-proportion z-test:
    remove draws
    non-draw matches = H + A
    p-hat = H / non-draw matches
    compare p-hat to 0.50
    calculate z-score and p-value

print all results
```

To reproduce the results, run:

```powershell
python inference_analysis.py
```
