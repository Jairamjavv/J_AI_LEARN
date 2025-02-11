import pandas as pd

data = {
    "Subject": ["Math", "Math", "Science", "Science", "Math", "Science"],
    "Grade": ["A", "B", "A", "C", "B", "B"],
    "Score": [90, 80, 95, 75, 85, 82],
}

df = pd.DataFrame(data)

# applying crosstabs - creating freq table for grades column
grades_freq_df = pd.crosstab(index=df["Subject"], columns=df["Grade"])

# Crosstab with values and aggregation
grades_aggregate_df = pd.crosstab(
    df["Subject"], df["Grade"], values=df["Score"], aggfunc="median"
)
print(grades_aggregate_df)

# Crosstab with normalization
ct_norm = pd.crosstab(df["Subject"], df["Grade"], normalize="index")  # Normalize by row
