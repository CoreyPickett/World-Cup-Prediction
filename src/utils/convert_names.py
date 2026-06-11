## Utility Script to convert all Countires to current names for accurate location tracking

# Import libraries
import pandas as pd

# Read results and former name files
results = pd.read_csv("data/raw/results.csv")
names = pd.read_csv("data/raw/former_names.csv")

# Build mapping of former → current
mapping = dict(zip(names["former"], names["current"]))

# Normalise location function
def normalise(country):
    return mapping.get(country, country)

# Apply to location country field
results["country"] = results["country"].apply(normalise)

# Save cleaned dataset
results.to_csv("data/processed/results_named.csv", index=False)
