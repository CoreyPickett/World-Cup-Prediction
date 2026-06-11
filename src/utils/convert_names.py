## Utility Script to convert all Countires to current names for accurate location tracking

# Import libraries
import pandas as pd

# Read results and former name files
results = pd.read_csv("data/raw/results.csv")
location_map = pd.read_csv("data/raw/former_names.csv")

# Mapping of former names to current
mapping = dict(zip(results["former"], results["current"]))

# Normalise location function:
    # Takes location and matches former name to current name
def normalise(country):
    return location_map.get(country, country)

# Normalise countries
results["country"] = results["country"].apply(normalise)

# Create CSV to save normalised team name results
results.to_csv("data/processed/results_named.csv", index=False)