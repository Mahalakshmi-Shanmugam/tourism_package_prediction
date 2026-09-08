import pandas as pd
import os
DATA_PATH = "tourism_project/data/tourism.csv"

EXPECTED_COLUMNS = [
    "CustomerID", "ProdTaken", "Age", "TypeofContact", "CityTier",
    "Occupation", "Gender", "NumberOfPersonVisiting", "PreferredPropertyStar",
    "MaritalStatus", "NumberOfTrips", "Passport", "OwnCar",
    "NumberOfChildrenVisiting", "Designation", "MonthlyIncome",
    "PitchSatisfactionScore", "ProductPitched", "NumberOfFollowups",
    "DurationOfPitch"
]

def validate_and_summarize_data(file_path):
    print(f"Loading data from: {file_path}")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")

    df = pd.read_csv(file_path)

    print("--- Data Validation ---")
    # 1. Check for expected columns
    missing_columns = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {missing_columns}")
    print("All expected columns are present.")

    # 2. Check for unexpected columns (optional, but good practice)
    unexpected_columns = [col for col in df.columns if col not in EXPECTED_COLUMNS]
    if unexpected_columns:
        print(f"Warning: Unexpected columns found: {unexpected_columns}")

    print("\n--- Data Summary ---")
    print("DataFrame Info:")
    df.info()
    print("\nDataFrame Description:")
    print(df.describe(include='all'))
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nData validation and summary complete.")

if __name__ == "__main__":
    # Ensure the script is run from the root of the repository
    # or adjust DATA_PATH if the script's execution context changes
    validate_and_summarize_data(DATA_PATH)
