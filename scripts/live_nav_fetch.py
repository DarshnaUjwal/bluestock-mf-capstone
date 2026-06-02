from pathlib import Path
import pandas as pd
import requests

# Create save location
RAW_DATA_PATH = Path("data/raw")

# Scheme codes provided in project instructions
scheme_codes = {
    "hdfc_top100": 125497,
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_largecap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841
}

print("\nFetching live NAV data...\n")

for fund_name, code in scheme_codes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = RAW_DATA_PATH / f"{fund_name}_live_nav.csv"

        nav_df.to_csv(output_file, index=False)

        print(f"Saved: {output_file.name}")

    except Exception as e:
        print(f"Error fetching {fund_name}: {e}")

print("\nLive NAV fetch completed.")