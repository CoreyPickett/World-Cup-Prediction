## Utility script to remove any matches which have not been played

# Import libraries
import pandas as pd

# Read in results
results = pd.read_csv("data/processed/results_named.csv")

# Remove rows with missing values and save to new file
clean = results.dropna(subset=["home_score", "away_score"])
clean.to_csv("data/processed/results_cleaned.csv", index=False)