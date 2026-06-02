from pathlib import Path
import pandas as pd

# Path to raw data folder
raw_path = Path("data/raw")

# Get all CSV files
csv_files = sorted(raw_path.glob("*.csv"))

print(f"\nFound {len(csv_files)} CSV files\n")

# Loop through each file
for file in csv_files:

    print("\n" + "=" * 70)
    print(f"FILE NAME: {file.name}")
    print("=" * 70)

    df = pd.read_csv(file)

    print("\nSHAPE")
    print(df.shape)

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nFIRST 5 ROWS")
    print(df.head())

    print("\nMISSING VALUES")
    print(df.isnull().sum())